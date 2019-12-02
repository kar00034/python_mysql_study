from configparser import ConfigParser


def read_db_config(filename='Config.ini', section='mysql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{} not found in {} file'.format(section, filename))
    return db
