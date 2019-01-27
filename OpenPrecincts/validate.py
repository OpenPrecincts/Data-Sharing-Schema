import logging, argparse, zipfile, sys
import pandas, geopandas
from .read import find_matching_feed_file

def validate_dataframe_columns(df, path, fields):
    '''
    '''
    expected_fields = set(fields)
    found_fields = set(df.columns)

    matching_fields = expected_fields & found_fields
    missing_fields = expected_fields - found_fields
    
    for matching_field in matching_fields:
        logging.debug('Found {} field in {}'.format(matching_field, path))
    
    for missing_field in missing_fields:
        logging.error('Missing {} field in {}'.format(missing_field, path))
    
    if missing_fields:
        return False
    
    return True

def validate_feed_textfile_fields(zf, path, fields):
    '''
    '''
    if path is None:
        return False
    
    dataframe = pandas.read_csv(zf.open(path))
    return validate_dataframe_columns(dataframe, path, fields)

def validate_feed_elections(zf):
    '''
    '''
    return validate_feed_textfile_fields(zf,
        find_matching_feed_file(zf, 'elections.csv'),
        ('election_id', 'state_id', 'election_date', 'election_type'))

def validate_feed_districts(zf):
    '''
    '''
    return validate_feed_textfile_fields(zf,
        find_matching_feed_file(zf, 'districts.csv'),
        ('district_id', 'state_id', 'district_plan', 'district_name',
        'chamber_name', 'shape_id', 'source_id'))

def validate_feed_precincts(zf):
    '''
    '''
    return validate_feed_textfile_fields(zf,
        find_matching_feed_file(zf, 'precincts.csv'),
        ('election_id', 'district_id', 'county_id', 'county_name',
        'precinct_name', 'shape_id', 'source_id'))

def validate_feed_sources(zf):
    '''
    '''
    return validate_feed_textfile_fields(zf,
        find_matching_feed_file(zf, 'sources.csv'),
        ('source_id', 'source_name', 'source_url'))

def validate_feed_shapes(zf):
    '''
    '''
    shapes_path = find_matching_feed_file(zf, 'shapes.shp')
    
    if shapes_path is None:
        return False
    
    dataframe = geopandas.read_file('/vsizip/{}/{}'.format(zf.filename, shapes_path))
    return validate_dataframe_columns(dataframe, shapes_path, ('shape_id', 'geometry'))

def validate_feed_file(feed_path):
    '''
    '''
    logging.info('Validating {}'.format(feed_path))

    all_checks = (validate_feed_elections, validate_feed_districts,
        validate_feed_precincts, validate_feed_sources, validate_feed_shapes)
    
    with zipfile.ZipFile(feed_path) as zf:
        check_results = [one_check(zf) for one_check in all_checks]
    
    if False in check_results:
        logging.error('Feed {} is not valid'.format(feed_path))
        return False
    
    logging.info('Feed {} is valid'.format(feed_path))
    return True

def main():
    parser = argparse.ArgumentParser(description='Validate feed.')
    parser.add_argument('feed_path', help='Input OpenPrecincts feed zip file')
    parser.add_argument('--verbose', '-v', help='Print lots of debug info',
        dest='loglevel', action='store_const', const=logging.DEBUG, default=logging.INFO)
    parser.add_argument('--quiet', '-q', help='Print nothing but errors',
        dest='loglevel', action='store_const', const=logging.ERROR, default=logging.INFO)
    
    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)

    is_valid = validate_feed_file(args.feed_path)
    exit(0 if is_valid else 1)
