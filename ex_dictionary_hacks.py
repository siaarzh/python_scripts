def testies():
    my_dict = {'url'  : ['url1'],  # list of urls
               'fnum' : [2],                 # number of files in each url
               'sheet': [None]}              # sheet number of every file per url, respectively to url
    print(my_dict['url'], my_dict['sheet'])
    
    my_dict['path'] = []
    temp_sheet = []
    for i, url in enumerate(my_dict['url']):
        for file in range(my_dict['fnum'][i]):
            path = url+'_'+str(file+1)
            print('extracting {}'.format(path))
            my_dict['path'].append(path)
            temp_sheet.append(my_dict['sheet'][i])
    my_dict['sheet'] = temp_sheet
    print(my_dict)

if __name__ == "__main__":
    testies()