import geopandas, pandas, zipfile, collections

Feed = collections.namedtuple('Feed',
    ('elections', 'districts', 'candidates', 'precincts', 'sources', 'shapes'))

def load_feed(path):
    '''
    '''
    with zipfile.ZipFile(path) as zf:
        with zf.open('elections.csv') as f:
            elections = pandas.read_csv(f)
        with zf.open('districts.csv') as f:
            districts = pandas.read_csv(f)
        with zf.open('candidates.csv') as f:
            candidates = pandas.read_csv(f)
        with zf.open('precincts.csv') as f:
            precincts = pandas.read_csv(f)
        with zf.open('sources.csv') as f:
            sources = pandas.read_csv(f)

    shapes = geopandas.read_file(f'/vsizip/{path}/shapes.shp')
    
    return Feed(elections, districts, candidates, precincts, sources, shapes)

def add_geometry(data_frame, shapes_frame):
    '''
    '''
    output_frame = pandas.merge(data_frame, shapes_frame, on='shape_id', how='left')
    return geopandas.GeoDataFrame(output_frame, crs=shapes_frame.crs)
