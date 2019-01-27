import geopandas, pandas, zipfile, collections
from .read import find_matching_feed_file

Feed = collections.namedtuple('Feed',
    ('elections', 'districts', 'candidates', 'precincts', 'sources', 'shapes'))

def load_feed(feed_path):
    '''
    '''
    with zipfile.ZipFile(feed_path) as zf:
        elections_path = find_matching_feed_file(zf, 'elections.csv')
        districts_path = find_matching_feed_file(zf, 'districts.csv')
        candidates_path = find_matching_feed_file(zf, 'candidates.csv')
        precincts_path = find_matching_feed_file(zf, 'precincts.csv')
        sources_path = find_matching_feed_file(zf, 'sources.csv')
        shapes_path = find_matching_feed_file(zf, 'shapes.shp')

        with zf.open(elections_path) as f:
            elections = pandas.read_csv(f)
        with zf.open(districts_path) as f:
            districts = pandas.read_csv(f)
        with zf.open(candidates_path) as f:
            candidates = pandas.read_csv(f)
        with zf.open(precincts_path) as f:
            precincts = pandas.read_csv(f)
        with zf.open(sources_path) as f:
            sources = pandas.read_csv(f)

    shapes = geopandas.read_file(f'/vsizip/{feed_path}/{shapes_path}')
    return Feed(elections, districts, candidates, precincts, sources, shapes)

def add_geometry(data_frame, shapes_frame):
    '''
    '''
    output_frame = pandas.merge(data_frame, shapes_frame, on='shape_id', how='left')
    return geopandas.GeoDataFrame(output_frame, crs=shapes_frame.crs)
