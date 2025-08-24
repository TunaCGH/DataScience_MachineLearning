'''
pd.Series.cat is an accessor object for categorical properties of the Series values.

When converted to the 'category' dtype, the memory usage of the Series is reduced (upto 90% less memory), 
and operations on the Series can be performed more efficiently.


Flow of contents:
0. Creat a Categorical Series: pd.Series(dtype='category'), .astype('category'), pd.Categorical()
1. Core attributes: .cat.categories, .cat.codes, .cat.ordered
2. Adding and Removing: .cat.add_categories(), 
                        .cat.remove_categories(), .cat.remove_unused_categories(), 
                        .cat.set_categories()
3. Renaming: .cat.rename_categories()
4. Reordering: .cat.reorder_categories()
5. Ordered categories: .cat.as_ordered() (Support meaningful min(), max(), and sorting operations)
6. Unordered categories: .cat.as_unordered() (Treat categories as nominal with no inherent order)
'''

import pandas as pd
import numpy as np

#---------------------------------------------------------------------------------------------------------------#
#-------------------------------------- 0. Create a Categorical Series -----------------------------------------#
#---------------------------------------------------------------------------------------------------------------#

#############################################
## Using pd.Series() with dtype='category' ##
#############################################

s_gender = pd.Series(["M", "M", "F", "M", "LGBTQ", "F", "M", "F", "LGBTQ", "M"], dtype = 'category')

print(s_gender)
# 0        M
# 1        M
# 2        F
# 3        M
# 4    LGBTQ
# 5        F
# 6        M
# 7        F
# 8    LGBTQ
# 9        M
# dtype: category
# Categories (3, object): ['F', 'LGBTQ', 'M']


######################################
## Using .astype('category') method ##
######################################

s_gender = pd.Series(["M", "M", "F", "M", "LGBTQ", "F", "M", "F", "LGBTQ", "M"])

'''
How .astype('category') works:
- Converts the Series to a categorical type.
- Categories are stored as a separate array, which saves memory.
- Useful for columns with a limited number of unique values.
- Categories are ordered from A-Z or increasing order.
'''

s_gender = s_gender.astype('category')
print(s_gender)
# 0        M
# 1        M
# 2        F
# 3        M
# 4    LGBTQ
# 5        F
# 6        M
# 7        F
# 8    LGBTQ
# 9        M
# dtype: category
# Categories (3, object): ['F', 'LGBTQ', 'M']


####################################
## Using pd.Categorical() method  ##
####################################

'''
pd.Categorical() is used to create categorical data from a Series.

It allows you to specify categories and their order, 
which can be useful for memory efficiency and performance 
when dealing with columns that have a limited number of unique values.

It's an improved version of .astype('category') that provides more control over the categories.

Note: missing values like NaN or None are not included in the categories by default.
'''

'''
By default, the ordered=False, meaning categories are unordered.
'''

'''
NOTE: THIS WILL NOT CREATE A pd.Series OBJECT, IT CREATES A pd.Categorical OBJECT.
=> MUST WRAP IT IN A pd.Series() TO GET A CATEGORICAL SERIES.
'''

#---------------------------
## string gender example
#---------------------------

lst_gender = ["M", "M", "F", "M", "LGBTQ", "F", "M", "F", "LGBTQ", "M"]

## With ordered = False
s_gender_categ = pd.Series(pd.Categorical(lst_gender, ordered = False))
print(s_gender_categ)
# 0        M
# 1        M
# 2        F
# 3        M
# 4    LGBTQ
# 5        F
# 6        M
# 7        F
# 8    LGBTQ
# 9        M
# dtype: category
# Categories (3, object): ['F', 'LGBTQ', 'M']


## With ordered = True
s_gender_categ = pd.Series(pd.Categorical(
    values = lst_gender,
    categories = ["LGBTQ", "F", "M"],  # Specify the order of categories
    ordered = True  # Set to True if you want to treat categories as ordered
))
print(s_gender_categ)
# 0        M
# 1        M
# 2        F
# 3        M
# 4    LGBTQ
# 5        F
# 6        M
# 7        F
# 8    LGBTQ
# 9        M
# dtype: category
# Categories (3, object): ['LGBTQ' < 'F' < 'M']

#---------------------------
## numeric example with NaN
#---------------------------

lst_price_levels = [1, 1, 3, 2, 5, 2, None, 4, 4, np.nan, 3]

## With ordered = False
s_price_levels_categ = pd.Series(pd.Categorical(lst_price_levels, ordered = False))
print(s_price_levels_categ)
# 0       1
# 1       1
# 2       3
# 3       2
# 4       5
# 5       2
# 6     NaN
# 7       4
# 8       4
# 9     NaN
# 10      3
# dtype: category
# Categories (5, int64): [1, 2, 3, 4, 5]
'''Here, the NaN and None values are not included in the categories.'''


## With ordered = True
s_price_levels_categ = pd.Series(pd.Categorical(
    values = lst_price_levels,
    categories = [1, 2, 3, 4, 5], # Define the level
    ordered = True  # Set to True if you want to treat categories as ordered
))
print(s_price_levels_categ)
# 0       1
# 1       1
# 2       3
# 3       2
# 4       5
# 5       2
# 6     NaN
# 7       4
# 8       4
# 9     NaN
# 10      3
# dtype: category
# Categories (5, int64): [1 < 2 < 3 < 4 < 5]


#---------------------------------------------------------------------------------------------------------------#
#------------------------------------------ 1. Core attributes -------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#

s_gender = pd.Categorical(["M", "M", "F", "M", "LGBTQ", "F", "M", "F", "LGBTQ", "M"])

s_levels = pd.Categorical(
    values = [1, 1, 3, 2, 5, 2, None, 4, 4, np.nan, 3],
    categories = [1, 2, 3, 4, 5],
    ordered = True
)

#####################
## .cat.categories ##
#####################
# Returns the categories of the categorical Series.

print(s_gender.cat.categories)