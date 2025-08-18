'''
Pandas Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). 
It is similar to a column in a spreadsheet or a SQL table.

Sometimes, can consider it as a dictionary-like structure where each element has a unique label (index).
Or like numpy 1D array with additional features like labels.


Flow of contents
1. Creating a Series: from a list, dictionary, ndarray or scalar value; with indexing.
2. Accessing elements: using index labels or positions.
3. Dtype
4. Some import Series attributes
5. Vectorized Operations: arithmetic operations, statistical methods, and more.
6. Name attributes: setting and getting the name of the Series.
'''

import pandas as pd

#-------------------------------------------------------------------------------------------------------------#
#---------------------------------------- 1. Creating a Series -----------------------------------------------#
#-------------------------------------------------------------------------------------------------------------#

#################
## From a list ##
#################

#---------------
## Without index labels, 
## pandas will create a default integer index starting from 0.
#----------------

s = pd.Series(data = [1, 2, 3, 4, 5])

print(s)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

#----------------
## With custom index labels
#----------------

s = pd.Series(data = [1, 2, 3, 4, 5], index = ['one', 'two', 'three', 'four', 'five'])

print(s)
# one      1
# two      2
# three    3
# four     4
# five     5
# dtype: int64


####################
## From a ndarray ##
####################

import numpy as np

s = pd.Series(data = np.random.rand(5), index = ['a', 'b', 'c', 'd', 'e'])

print(s)
# a    0.503145
# b    0.622401
# c    0.766209
# d    0.962831
# e    0.794495
# dtype: float64


#######################
## From a dictionary ##
#######################

# The keys will be used as index labels, and the values will be the data in the Series.
s = pd.Series(data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

print(s)
# a    1
# b    2
# c    3
# d    4
# e    5
# dtype: int64


#########################
## From a scalar value ##
#########################

s = pd.Series(data = 5, index = ['a', 'b', 'c', 'd', 'e'])

print(s)
# a    5
# b    5
# c    5
# d    5
# e    5
# dtype: int64