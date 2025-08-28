'''
Pandas offers many functions to read data from various file formats into DataFrames.

Flow of contents:
1. pd.read_csv() - Read CSV files
2. pd.read_excel() - Read Excel files
3. pd.read_json() - Read JSON files
4. pd.read_xml() - Read XML files
'''

import pandas as pd

#---------------------------------------------------------------------------------------------------------#
#----------------------------------------- 1. pd.read_csv() ----------------------------------------------#
#---------------------------------------------------------------------------------------------------------#

'''
read_csv() is the most commonly used pandas I/O function, designed to read CSV files into DataFrames. 
It supports over 50 parameters for comprehensive data control.

Detailed documentation: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv

File parameters:
+ filepath_or_buffer: Accepts file paths, URLs, or file-like objects
+ sep/delimiter: Field separator (default: ',')
+ encoding: Text encoding (utf-8, latin-1, etc.)
+ compression: Automatic detection ('infer') or specific formats ('gzip', 'bz2', 'zip')
+ skiprows: Number of rows to skip at the start
+ skipfooter: Number of rows to skip at the end
+ nrows: Number of rows to read

Data Structure Control parameters:
+ header: Row number(s) for column names ('infer', int, list, None)
+ names: Custom column names list
+ index_col: Column(s) to use as row labels
+ usecols: Subset of columns to return

NA values handling:
+ na_values: Additional strings to recognize as NA/NaN
+ keep_default_na: Whether to include default NA values
+ na_filter: Detect missing values (default: True)

Data Type Management
+ dtype: Specify data types for columns
+ converters: Custom functions for value conversion
+ parse_dates: Parse date columns automatically
'''

#################
## Basic Usage ##
#################

df = pd.read_csv('05_Pandas_DataR_dataframe/01_Pandas_python_style/data/emp.csv')

print(df)
#    id      name  salary  start_date        dept
# 0   1      Rick  623.30  2012-01-01          IT
# 1   2       Dan  515.20  2013-09-23  Operations
# 2   3  Michelle  611.00  2014-11-15          IT
# 3   4      Ryan  729.00  2014-05-11          HR
# 4   5      Gary  843.25  2015-03-27     Finance
# 5   6      Nina  578.00  2013-05-21          IT
# 6   7     Simon  632.80  2013-07-30  Operations
# 7   8      Guru  722.50  2014-06-17     Finance

########################
## Specify index_col= ##
########################

df = pd.read_csv(
    filepath_or_buffer = '05_Pandas_DataR_dataframe/01_Pandas_python_style/data/emp.csv', 
    index_col = 'id'
)

print(df)
#         name  salary  start_date        dept
# id                                          
# 1       Rick  623.30  2012-01-01          IT
# 2        Dan  515.20  2013-09-23  Operations
# 3   Michelle  611.00  2014-11-15          IT
# 4       Ryan  729.00  2014-05-11          HR
# 5       Gary  843.25  2015-03-27     Finance
# 6       Nina  578.00  2013-05-21          IT
# 7      Simon  632.80  2013-07-30  Operations
# 8       Guru  722.50  2014-06-17     Finance
'''Now the 'id' column is set as the DataFrame index.'''

######################
## Specify usecols= ##
######################

df = pd.read_csv(
    filepath_or_buffer = '05_Pandas_DataR_dataframe/01_Pandas_python_style/data/emp.csv', 
    usecols = ['name', 'salary', 'dept']
)

print(df)
#        name  salary        dept
# 0      Rick  623.30          IT
# 1       Dan  515.20  Operations
# 2  Michelle  611.00          IT
# 3      Ryan  729.00          HR
# 4      Gary  843.25     Finance
# 5      Nina  578.00          IT
# 6     Simon  632.80  Operations
# 7      Guru  722.50     Finance

####################
## Specify dtype= ##
####################

df = pd.read_csv(
    filepath_or_buffer = '05_Pandas_DataR_dataframe/01_Pandas_python_style/data/emp.csv', 
    usecols=['name', 'salary', 'dept'],
    dtype = {
        'name': 'str', # If set as 'string', it will be "string[python]", not "object"
        'salary': 'float64',
        'dept': 'category'
    }
)

print(df)
#        name  salary        dept
# 0      Rick  623.30          IT
# 1       Dan  515.20  Operations
# 2  Michelle  611.00          IT
# 3      Ryan  729.00          HR
# 4      Gary  843.25     Finance
# 5      Nina  578.00          IT
# 6     Simon  632.80  Operations
# 7      Guru  722.50     Finance

print(df.dtypes)
# name        object
# salary     float64
# dept      category
# dtype: object