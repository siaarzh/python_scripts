# Saving and importing sources configuration files using Parameter File (INI)

def save_sources_config(data:dict, output_path:str, file_format:str='json'):
    """
    Save your table_hierarchy data into file.
    
    :param dict data: Table hierarchy dictionary.
    :param str output_path: Destination to save file.
    :param str file_format: Output format, can be either 'json' or 'ini'
    """
    
    import os # TODO: move import out of function
    
    
    config = configparser.ConfigParser()
    
    for key1, data1 in data.items():
        config[key1] = {}
        for key2, data2 in data1.items():
            config[key1]["{}".format(key2)] = str(data2)
            
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    if file_file_format == 'json':
        
        import json # TODO: move import out of function
        
        with open(output_path, 'w') as configfile:
            json.dump(data, configfile, indent=2, ensure_ascii=False)
    
    elif file_file_format in ['ini']:
        
        import configparser

        config = configparser.ConfigParser()

        for key1, data1 in data.items():
            config[key1] = {}
            for key2, data2 in data1.items():
                config[key1]["{}".format(key2)] = str(data2)
        
        with open(output_path, 'w') as configfile:
            config.write(configfile)
    
    else:
        raise ValueError("file_file_format can only be [ json | ini ]")

save_to_config(table_hierarchy)

def read_from_config(source:str, file_format:str='auto'):
    """
    Read table_hierarchy data into dict.
    
    :param str source: Configuration file path.
    :param str file_format: File format, can be either 'ini', 'json' or 'auto' for automatic
                            selection based on file extension.
    """
    import os # TODO: move import out of method
    
    _, file_ext = os.path.splitext(file_path)
    
    if (file_format == 'auto' and file_ext in ['.ini', '.conf']) or file_format in ['ini', 'conf']:
    
        from configparser import ConfigParser # TODO: remove this comment, otherwise this import is fine
        import ast  # TODO: move import out of method

        parser = ConfigParser()
        parser.read(source)

        data = {}

        for section in parser.sections():
            data[section] = {}
            for k, val in parser.items(section):
                if k in ['index_col', 'store']:
                    data[section][k] = str(val)
                else:
                    data[section][k] = ast.literal_eval(str(val))
    
    elif (file_format == 'auto' and file_ext in ['.json']) or file_format in ['json']:
        
        import json # TODO: move import out of method
        
        with open(source, 'r') as configfile:
        data = json.load(configfile)
    
    else:
        
        raise ValueError("Unknown format: {}".format(file_format))
        
        
    
    return data

new_dict_from_config = read_from_config('data.ini')

new_dict_from_config == table_hierarchy