'''
pandas has an options API configure and customize global behavior related to DataFrame display, 
data behavior and more.

#########################################

Flow of contents:

1. All available options: pd.describe_option()

2. Getting, Setting and Resetting options: 
   + Getting: pd.get_option() 
   + Setting: pd.set_option()
   + Resetting: pd.reset_option()

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


#-------------------------------------------------------------------------------------------------------#
#-------------------------------------- 1. All available options ---------------------------------------#
#-------------------------------------------------------------------------------------------------------#

'''
Use pd.describe_option() to see all available options in pandas.
'''

print(pd.describe_option())
# display.max_columns : int
#     If max_cols is exceeded, switch to truncate view. Depending on
#     `large_repr`, objects are either centrally truncated or printed as
#     a summary view. 'None' value means unlimited.

#     In case python/IPython is running in a terminal and `large_repr`
#     equals 'truncate' this can be set to 0 or None and pandas will auto-detect
#     the width of the terminal and print a truncated object which fits
#     the screen width. The IPython notebook, IPython qtconsole, or IDLE
#     do not run in a terminal and hence it is not possible to do
#     correct auto-detection and defaults to 20.
#     [default: 0] [currently: 0]
# display.max_colwidth : int or None
#     The maximum width in characters of a column in the repr of
#     a pandas data structure. When the column overflows, a "..."
#     placeholder is embedded in the output. A 'None' value means unlimited.
#     [default: 50] [currently: 50]
'''And more...'''


#-------------------------------------------------------------------------------------------------------#
#---------------------------- 2. Getting, Setting and Resetting options --------------------------------#
#-------------------------------------------------------------------------------------------------------#

#####################
## pd.get_option() ##
#####################
'''Use pd.get_option() to get the current value of a specific option.'''

print(pd.get_option("display.max_rows"))        # 60
print(pd.get_option("display.max_columns"))     # 0
print(pd.get_option("display.width"))           # 80
print(pd.get_option("display.precision"))       # 6
print(pd.get_option("mode.sim_interactive"))    # False

#####################
## pd.set_option() ##
#####################
'''Use pd.set_option() to set a specific option to a new value.'''

pd.get_option("display.max_rows") # 60

# Set new max_rows option
pd.set_option("display.max_rows", 30)

# Check the updated value
pd.get_option("display.max_rows") # 30

#######################
## pd.reset_option() ##
#######################
'''Use pd.reset_option() to reset a specific option to its default value.'''

print(pd.get_option("mode.sim_interactive"))    # False

pd.set_option("mode.sim_interactive", True)
print(pd.get_option("mode.sim_interactive"))    # True

# Reset to default value
pd.reset_option("mode.sim_interactive")

# Check the reset value
print(pd.get_option("mode.sim_interactive"))    # False


#-------------------------------------------------------------------------------------------------------#
#----------------------- 3. Setting startup options in Python/IPython environment ----------------------#
#-------------------------------------------------------------------------------------------------------#

'''
Pandas and Python support setting startup options via configuration files.
So that you don't have to set them manually every time you start a new session.

Check the tutorial here: 
https://pandas.pydata.org/docs/user_guide/options.html#setting-startup-options-in-python-ipython-environment
'''


#-------------------------------------------------------------------------------------------------------#
#------------------------------------- 4. Frequently used options --------------------------------------#
#-------------------------------------------------------------------------------------------------------#