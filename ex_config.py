from configparser import ConfigParser


def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

def update_config(filename, section, **kwargs):
    # This will REMOVE all values in 'section' and fill
    # it with **kwargs
    parser = ConfigParser()
    parser.read(filename)

    parser[section] = kwargs

    with open(filename, 'w') as configfile:
        parser.write(configfile)

def remove_key(d, key):
    # This will remove a key:value pair in a dictionary
    r = dict(d)
    try:
        del r[key]
    except:
        pass
    return r

def remove_section(filename, section): # TODO: Remove if not used
    # This will remove a 'section' from the ini file
    parser = ConfigParser()
    parser.read(filename)

    parser.remove_section(section)

    with open(filename, 'w') as configfile:
        parser.write(configfile)

def change_value(filename, section, **kwargs): # TODO: Remove if not used
    # This will set key-values in 'section' without deleting
    # existing content
    parser = ConfigParser()
    parser.read(filename)
    for key, value in kwargs.items():
        parser.set(section, key, value)

    with open(filename, 'w') as configfile:
        parser.write(configfile)

def swap_values(filename, section, param1, param2):
    # Swaps values of 'section' between keys param1 and param2
    parser = ConfigParser()
    parser.read(filename)

    try:
        parser[section][param2], parser[section][param1] \
            = parser[section][param1], parser[section][param2]
    except Exception as e:
        raise e

    with open(filename, 'w') as configfile:
        parser.write(configfile)