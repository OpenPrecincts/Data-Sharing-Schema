import logging, os

def find_matching_feed_file(zf, expected_name):
    ''' Return matching path from feed ZipFile object with the expected name
    '''
    role, _ = os.path.splitext(os.path.basename(expected_name))
    
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
