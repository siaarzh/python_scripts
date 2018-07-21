import numpy as np
import pandas as pd


my_test_dict = {'table1':{'url': 'example.com', 'path': '/some/path/file.xls'}}

print(my_test_dict)

df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo' })

my_test_dict['table1']['df'] = df2

print(my_test_dict)