from configparser import ConfigParser


def update_config(filename, section, **args):
    parser = ConfigParser()
    parser.read(filename)

    parser[section] = args

    with open(filename, 'w') as configfile:
        parser.write(configfile)


def remove_key(d, key):
    r = dict(d)
    try:
        del r[key]
    except:
        pass
    return r

def_args = {'rank': 22,         # 30
            'maxIter': 5,       # 10
            'regParam': 0.5}    # 0.1

parse_args = {'app_name': 'app42',
              'rank': None,
              'maxIter': 7,
              'regParam': None}

# Update default args with new non-null parameters
parse_args = remove_key(parse_args, 'app_name')
for key, value in parse_args.items():
    if not parse_args[key]:
        parse_args[key] = def_args[key]
    else:
        pass

update_config(filename='predict.ini', section='parameters', **parse_args)


