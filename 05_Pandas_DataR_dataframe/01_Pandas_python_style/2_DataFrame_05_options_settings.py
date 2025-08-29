'''
pandas has an options API configure and customize global behavior related to DataFrame display, 
data behavior and more.

#########################################

Flow of contents:

1. All available options: pd.describe_option()
2. Getting, Setting and Resetting options: pd.get_option(), pd.set_option(), pd.reset_option()
3. Setting startup options in Python/IPython environment
4. Frequently used options: max_rows, max_columns, display.width
5. Number formatting
6. Unicode formatting

Detailed documentation: https://pandas.pydata.org/docs/user_guide/options.html#
'''

import pandas as pd

df_medals = pd.read_csv(
    filepath_or_buffer = "05_Pandas_DataR_dataframe/data/medals.csv",
    skiprows = 4
)

# Make all columns categorical
df_medals = df_medals.astype("category")

df_medals.head(3)
#    Year      City    Sport      Discipline  NOC       Event Event gender   Medal
# 0  1924  Chamonix  Skating  Figure skating  AUT  individual            M  Silver
# 1  1924  Chamonix  Skating  Figure skating  AUT  individual            W    Gold
# 2  1924  Chamonix  Skating  Figure skating  AUT       pairs            X    Gold

df_medals.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 2311 entries, 0 to 2310
# Data columns (total 8 columns):
#  #   Column        Non-Null Count  Dtype   
# ---  ------        --------------  -----   
#  0   Year          2311 non-null   category
#  1   City          2311 non-null   category
#  2   Sport         2311 non-null   category
#  3   Discipline    2311 non-null   category
#  4   NOC           2311 non-null   category
#  5   Event         2311 non-null   category
#  6   Event gender  2311 non-null   category
#  7   Medal         2311 non-null   category
# dtypes: category(8)
# memory usage: 24.8 KB