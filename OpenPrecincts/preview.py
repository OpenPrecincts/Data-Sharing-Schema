import logging, argparse
import contextily, matplotlib.pyplot, matplotlib.ticker, mercantile
from . import load_feed

# Constant strings found in data feeds
DEM, REP, YES, NO = 'Dem', 'Rep', 'Yes', 'No'

MAP_URL = contextily.sources.ST_TONER_LITE
MAP_URL = 'https://cartodb-basemaps-a.global.ssl.fastly.net/light_nolabels/tileZ/tileX/tileY.png'

def get_plot_zoomlevel(plot):
    ''' Walk down zoom levels until we hit a good value for zoom
    '''
    def get_plot_bounds(plot):
        ''' Get plot bounds in degrees
        '''
        xmin, xmax = plot.xaxis.get_view_interval()
        ymin, ymax = plot.yaxis.get_view_interval()
        minlon, minlat = mercantile.lnglat(xmin, ymin)
        maxlon, maxlat = mercantile.lnglat(xmax, ymax)
    
        return minlon, minlat, maxlon, maxlat

    def get_plot_tile_dimensions(plot):
        ''' Calculate size of plot in tiles at 96ppi
        '''
        plot_pos_bbox = plot.get_position()
        fig_width_tiles, fig_height_tiles = plot.figure.get_size_inches() * 96 / 256
        plot_width_tiles = fig_width_tiles * (plot_pos_bbox.xmax - plot_pos_bbox.xmin)
        plot_height_tiles = fig_height_tiles * (plot_pos_bbox.ymax - plot_pos_bbox.ymin)
    
        return plot_width_tiles, plot_height_tiles

    minlon, minlat, maxlon, maxlat = get_plot_bounds(plot)
    plot_width_tiles, plot_height_tiles = get_plot_tile_dimensions(plot)
    
    for zoom in range(18, 0, -1):
        ul_tile = mercantile.tile(minlon, maxlat, zoom)
        lr_tile = mercantile.tile(maxlon, minlat, zoom)
        if (lr_tile.x - ul_tile.x) <= round(plot_width_tiles):
            break
        if (lr_tile.y - ul_tile.y) <= round(plot_height_tiles):
            break
    
    logging.info('add_basemap(): loading tiles at zoom {z}'.format(z=zoom))

    return zoom

def add_basemap(plot):
    '''
    '''
    zoom = get_plot_zoomlevel(plot)
    
    xmin, xmax, ymin, ymax = plot.axis()
    basemap, extent = contextily.bounds2img(xmin, ymin, xmax, ymax,
        zoom=zoom, url=MAP_URL)

    plot.imshow(basemap, extent=extent, interpolation='bilinear')
    plot.axis((xmin, xmax, ymin, ymax))

def get_axis_viewport(minlon, minlat, maxlon, maxlat):
    '''
    '''
    x0, y0 = mercantile.xy(minlon, minlat)
    x1, y1 = mercantile.xy(maxlon, maxlat)

    buffer = max(x1 - x0, y1 - y0) * .1
    xmin, ymin = x0 - buffer, y0 - buffer
    xmax, ymax = x1 + buffer, y1 + buffer
    
    return (xmin, xmax, ymin, ymax)

def format_func(meters, _):
    ''' Format meters as degrees in matplotlib.ticker.FuncFormatter
    '''
    if meters < 0:
        # assume x values in western hemisphere
        degrees, _ = mercantile.lnglat(meters, 0)
    else:
        # assume y values in northern hemisphere
        _, degrees = mercantile.lnglat(0, meters)
    
    return '{deg:+.3f}°'.format(deg=degrees)

def shapes_plot(shapes, size=(9, 6), bounds=None):
    ''' Create a simple locator map for shapes from a feed
    '''
    figure, plot = matplotlib.pyplot.subplots(figsize=size)
    
    mercs = shapes.to_crs(epsg=3857)
    mercs.plot(ax=plot, color='#ff990020')
    mercs.boundary.plot(ax=plot, color='#00000080', linestyle='dotted', linewidth=1)

    return finish_plot(plot, bounds)

def parties_plot(shapes, size=(9, 6), bounds=None):
    ''' Create a simple locator map for partisan shapes from a feed
    '''
    _, plot = matplotlib.pyplot.subplots(figsize=size)
    
    mercs = shapes.to_crs(epsg=3857)
    party = mercs.candidate_party
    
    if (party == DEM).any():
        mercs[party == DEM].plot(ax=plot, color='#0049a899')

    if (party == REP).any():
        mercs[party == REP].plot(ax=plot, color='#c71c3699')

    if ((party != DEM) & (party != REP)).any():
        mercs[(party != DEM) & (party != REP)].plot(ax=plot, color='#6d5c6599')

    mercs.boundary.plot(ax=plot, color='#ffffff80', linestyle='dotted', linewidth=1)
    
    return finish_plot(plot, bounds)

def finish_plot(plot, bounds):
    '''
    '''
    plot.set_aspect('equal')
    
    if bounds is not None:
        plot.axis(get_axis_viewport(*bounds))
    
    for axis in (plot.xaxis, plot.yaxis):
        low, high = axis.get_view_interval()
        lerp = lambda x: low * (1 - x) + high * x
        axis.set_ticks([lerp(x) for x in (.1, .3, .5, .7, .9)])
        axis.set_major_formatter(matplotlib.ticker.FuncFormatter(format_func))
    
    plot.figure.tight_layout(pad=.1)

    # Add basemap last so plot.get_position() is meaningful in inches
    add_basemap(plot)
    
    return plot

def main_feed():
    parser = argparse.ArgumentParser(description='Preview feed.')
    parser.add_argument('feed_path', help='Input OpenPrecincts feed zip file')
    parser.add_argument('preview_path', help='Output PDF, JPG, or PNG shapes preview file')
    
    args = parser.parse_args()
    feed = load_feed(args.feed_path)
    plot = shapes_plot(feed.shapes, size=(8, 10))
    plot.figure.savefig(args.preview_path)
