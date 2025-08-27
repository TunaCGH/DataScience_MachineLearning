'''
There are many ways to create a DataFrame in Pandas. Here are some of the most common methods:

1. From a dictionary of series
2. From a dictionary of lists or ndarrays
3. From a structured or record array
4. From a list of dictionaries
5. From a dictionary of tuples
6. From a list of namedtuples
7. From a list of dataclasses
8. Other constructors
'''

import pandas as pd
import numpy as np

#-------------------------------------------------------------------------------------------------------------#
#------------------------------------- 1. From a dictionary of series ----------------------------------------#
#-------------------------------------------------------------------------------------------------------------#

##################
## Step-by-step ##
##################

data_dict = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
}

df = pd.DataFrame(data_dict)
print(df)
#    one  two
# a  1.0  1.0
# b  2.0  2.0
# c  3.0  3.0
# d  NaN  4.0
'''Here, the dictionary keys become the column names'''

#####################
## Shorter version ##
#####################

df = pd.DataFrame(
    data ={
        "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
        "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
    }
)

print(df)
#    one  two
# a  1.0  1.0
# b  2.0  2.0
# c  3.0  3.0
# d  NaN  4.0


#-------------------------------------------------------------------------------------------------------------#
#--------------------------------- 2. From a dictionary of lists or ndarrays ---------------------------------#
#-------------------------------------------------------------------------------------------------------------#

################
## from lists ##
################

df = pd.DataFrame(
    data = {
        "column_1": [1, 3, 5, 7],
        "column_2": [2.0, 4.0, 6.0, 8.0],
        "column_3": ["a", "b", "c", "d"],
    }
)

print(df)
#    column_1  column_2 column_3
# 0         1       2.0        a
# 1         3       4.0        b
# 2         5       6.0        c
# 3         7       8.0        d

###################
## from ndarrays ##
###################

df = pd.DataFrame(
    data = {
        "column_1": np.array([1.5, 3.2, 5.7, 6.8]),
        "column_2": np.array([2, 4.9, 2.3, 1.2]),
    }
)

print(df)
#    column_1  column_2
# 0       1.5       2.0
# 1       3.2       4.9
# 2       5.7       2.3
# 3       6.8       1.2

##################
## Advanced way ##
##################

df_score = pd.DataFrame(
    data = {
        "name": ["Alice"]*3 + ["Susan"]*3,
        "subject": ["Math", "Science", "English"]*2,
        "score": np.array([85, 90, 88, 92, 95, 89]),
    }
)

print(df_score)
#     name  subject  score
# 0  Alice     Math     85
# 1  Alice  Science     90
# 2  Alice  English     88
# 3  Susan     Math     92
# 4  Susan  Science     95
# 5  Susan  English     89