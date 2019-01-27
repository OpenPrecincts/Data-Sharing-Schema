import logging, argparse, zipfile, os
import pandas, geopandas

def find_matching_feed_file(zf, role, expected_name):
    '''
    '''
    found_names = [name for name in zf.namelist()
        if os.path.basename(name).lower() == expected_name.lower()]
    
    if not found_names:
        logging.error('Missing {} file'.format(role))
        return None
    
    found_name, extra_names = found_names[0], found_names[1:]
    
    if extra_names:
        logging.warning('Found extra {} files: {}'.format(role, ', '.join(extra_names)))
    
    logging.debug('Found {} file: {}'.format(role, found_name))
    return found_name

def find_elections(zf):
    '''
    '''
    return find_matching_feed_file(zf, 'elections', 'elections.csv')

def find_districts(zf):
    '''
    '''
    return find_matching_feed_file(zf, 'districts', 'districts.csv')

def find_precincts(zf):
    '''
    '''
    return find_matching_feed_file(zf, 'precincts', 'precincts.csv')

def find_sources(zf):
    '''
    '''
    return find_matching_feed_file(zf, 'sources', 'sources.csv')

def find_shapes(zf):
    '''
    '''
    return find_matching_feed_file(zf, 'shapes', 'shapes.shp')

def validate_dataframe_columns(df, path, fields):
    '''
    '''
    is_valid = True
    expected_fields = set(fields)
    found_fields = set(df.columns)
    
    for matching_field in (expected_fields & found_fields):
        logging.debug('Found {} field in {}'.format(matching_field, path))
        is_valid &= True
    
    for missing_field in (expected_fields - found_fields):
        logging.error('Missing {} field in {}'.format(missing_field, path))
        is_valid = False
    
    return is_valid

def validate_feed_textfile_fields(zf, path, fields):
    '''
    '''
    dataframe = pandas.read_csv(zf.open(path))
    return validate_dataframe_columns(dataframe, path, fields)

def validate_feed_elections(zf, elections_path):
    '''
    '''
    return validate_feed_textfile_fields(zf, elections_path,
        ('election_id', 'state_id', 'election_date', 'election_type'))

def validate_feed_districts(zf, districts_path):
    '''
    '''
    return validate_feed_textfile_fields(zf, districts_path,
        ('district_id', 'state_id', 'district_plan', 'district_name',
        'chamber_name', 'shape_id', 'source_id'))

def validate_feed_precincts(zf, precincts_path):
    '''
    '''
    return validate_feed_textfile_fields(zf, precincts_path,
        ('election_id', 'district_id', 'county_id', 'county_name',
        'precinct_name', 'shape_id', 'source_id'))

def validate_feed_sources(zf, sources_path):
    '''
    '''
    return validate_feed_textfile_fields(zf, sources_path,
        ('source_id', 'source_name', 'source_url'))

def validate_feed_shapes(zf, shapes_path):
    '''
    '''
    dataframe = geopandas.read_file('/vsizip/{}/{}'.format(zf.filename, shapes_path))
    return validate_dataframe_columns(dataframe, shapes_path, ('shape_id', 'geometry'))

def validate_feed_file(feed_path):
    '''
    '''
    path_checks = [
        (find_elections, validate_feed_elections),
        (find_districts, validate_feed_districts),
        (find_precincts, validate_feed_precincts),
        (find_sources, validate_feed_sources),
        (find_shapes, validate_feed_shapes),
        ]
    
    logging.info('Validating {}'.format(feed_path))
    is_valid = True

    with zipfile.ZipFile(feed_path) as zf:
        for (find_path, validate_path) in path_checks:
            path = find_path(zf)
            if path:
                is_valid &= validate_path(zf, path)
            else:
                is_valid = False
    
    if is_valid:
        logging.info('Feed {} is valid'.format(feed_path))
    else:
        logging.error('Feed {} is not valid'.format(feed_path))
    
    return is_valid

def main():
    parser = argparse.ArgumentParser(description='Validate feed.')
    parser.add_argument('feed_path', help='Input OpenPrecincts feed zip file')
    parser.add_argument('--verbose', '-v', help='Print lots of debug info',
        dest='loglevel', action='store_const', const=logging.DEBUG, default=logging.INFO)
    parser.add_argument('--quiet', '-q', help='Print nothing but errors',
        dest='loglevel', action='store_const', const=logging.WARNING, default=logging.INFO)
    
    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel)

    is_valid = validate_feed_file(args.feed_path)
    exit(0 if is_valid else 1)
