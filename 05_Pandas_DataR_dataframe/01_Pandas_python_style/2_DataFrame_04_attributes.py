'''
Flow of contents:

1. Shape and Size attributes:
   + df.shape: Returns a tuple (rows, columns)
   + df.size: Returns total number of elements (rows * columns)
   + df.ndim: Returns number of dimensions (always 2 for DataFrame)

2. Data types and Structure attributes:
   + df.dtypes: Returns data types of each column
   + df.columns: Returns column labels
   + df.index: Returns row labels
   + df.axes: Returns a list of both row and column labels

3. Data Access attributes:
   + df.values: Returns the underlying numpy array of the DataFrame
   + df.T: Returns the transpose of the DataFrame
   + df.empty: Returns True if DataFrame is empty, else False

4. Memory and Performance attributes:
   + df.info(memory_usage = 'deep'): Provides a concise summary of the DataFrame
   + df.memory_usage(deep = True): Returns memory usage of each column

4. Advanced attributes:
   + df.attrs: Dictionary for storing custom metadata
   + df.style: Returns a Styler object for HTML/CSS formatting
   + df.flags: Configuration object controlling DataFrame behavior. 
'''

import pandas as pd

df_medals = pd.read_csv(
    filepath_or_buffer = "05_Pandas_DataR_dataframe/data/medals.csv",
    skiprows = 4
)


df_medals.head()
#    Year      City       Sport      Discipline  NOC       Event Event gender   Medal
# 0  1924  Chamonix     Skating  Figure skating  AUT  individual            M  Silver
# 1  1924  Chamonix     Skating  Figure skating  AUT  individual            W    Gold
# 2  1924  Chamonix     Skating  Figure skating  AUT       pairs            X    Gold
# 3  1924  Chamonix   Bobsleigh       Bobsleigh  BEL    four-man            M  Bronze
# 4  1924  Chamonix  Ice Hockey      Ice Hockey  CAN  ice hockey            M    Gold


df_medals.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 2311 entries, 0 to 2310
# Data columns (total 8 columns):
#  #   Column        Non-Null Count  Dtype 
# ---  ------        --------------  ----- 
#  0   Year          2311 non-null   int64 
#  1   City          2311 non-null   object
#  2   Sport         2311 non-null   object
#  3   Discipline    2311 non-null   object
#  4   NOC           2311 non-null   object
#  5   Event         2311 non-null   object
#  6   Event gender  2311 non-null   object
#  7   Medal         2311 non-null   object
# dtypes: int64(1), object(7)
# memory usage: 144.6+ KB

#------------------------------------------------------------------------------------------------------