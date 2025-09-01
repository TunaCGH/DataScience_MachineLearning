'''
df.select_dtypes(include=..., exclude=...) allows you to select columns in a DataFrame based on their data types.

include, exclude: scalar or list-like
=> A selection of dtypes or strings (column names) to be included/excluded. 
   At least one of these parameters must be supplied.
'''

########################

'''
To select all numeric types, use: 'np.number' or 'number'

To select strings you must use: object, 
but note that this will return all object dtype columns. 

To select datetimes, use: np.datetime64, 'datetime' or 'datetime64'

To select timedeltas, use: np.timedelta64, 'timedelta' or 'timedelta64'

To select Pandas categorical dtypes, use: 'category'

To select Pandas datetimetz dtypes, use: 'datetimetz' or 'datetime64[ns, tz]'
'''

import pandas as pd

df_emp = pd.read_csv(
    filepath_or_buffer = "05_Pandas_DataR_dataframe/data/emp.csv",
    parse_dates = ["start_date"],
    dtype = {"dept": "category"}
)

print(df_emp.dtypes)
# id                     int64
# name                  object
# salary               float64
# start_date    datetime64[ns]
# dept                category
# dtype: object