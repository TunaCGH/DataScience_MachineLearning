'''
pd.concat() and pd.merge() are two powerful functions in pandas used for combining DataFrames, 
but they serve different purposes and operate in different ways.

#########################################################

1. Concatenation:
   + pd.concat(axis = 0): used to stack DataFrames vertically (row-wise).
   + pd.concat(axis = 1): used to stack DataFrames horizontally (column-wise).

2. Merging:
   + pd.merge(how = 'inner'): only keeps rows whose keys are present in both DataFrames.
   + pd.merge(how = 'outer'): keeps all rows from both DataFrames, filling in NaNs for missing matches.
   + pd.merge(how = 'left'): keeps all rows from the left DataFrame and matches from the right DataFrame.
   + pd.merge(how = 'right'): keeps all rows from the right DataFrame and matches from the left DataFrame.
   + pd.merge(how = 'cross'): creates the Cartesian product of both DataFrames.
   + pd.merge(on = 'key'): merges DataFrames based on a common column (key).
   + pd.merge(left_on = 'key1', right_on = 'key2'): merges DataFrames based on different columns from each DataFrame.
   + pd.merge(left_index = True, right_index = True): merges DataFrames based on their index.
   + pd.merge(suffixes = ('_left', '_right')): adds suffixes to overlapping column names to differentiate them.
'''

import pandas as pd
import numpy as np

#------------------------------------------------------------------------------------------------------#
#---------------------------------------- 1. Concatenation --------------------------------------------#
#------------------------------------------------------------------------------------------------------#

# Create sample DataFrames
df_origin = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3']
})

df_ver_1 = pd.DataFrame({
    'A': ['A4', 'A5', 'A6', 'A7'],
    'B': ['B4', 'B5', 'B6', 'B7'],
    'C': ['C4', 'C5', 'C6', 'C7']
})

df_ver_2 = pd.DataFrame({
    'A': ['A8', 'A9', 'A10', 'A11'],
    'B': ['B8', 'B9', 'B10', 'B11'],
    'C': ['C8', 'C9', 'C10', 'C11']
})

df_hor_1 = pd.DataFrame({
    'D': ['D0', 'D1', 'D2', 'D3'],
    'E': ['E0', 'E1', 'E2', 'E3'],
    'F': ['F0', 'F1', 'F2', 'F3']
})

df_hor_2 = pd.DataFrame({
    'G': ['G0', 'G1', 'G2', 'G3'],
    'H': ['H0', 'H1', 'H2', 'H3'],
    'I': ['I0', 'I1', 'I2', 'I3']
})

###############################
##    pd.concat(axis = 0)    ##
###############################
''' Concatenate DataFrames vertically (row-wise) '''

# Original DataFrame
print(df_origin)
#     A   B   C
# 0  A0  B0  C0
# 1  A1  B1  C1
# 2  A2  B2  C2
# 3  A3  B3  C3

# Concatenate df_origin and df_ver_1 vertically
df_stack_ver = pd.concat(
    objs = [df_origin, df_ver_1],
    axis = 0,
    ignore_index = True # Reset index in the concatenated DataFrame
)
print(df_stack_ver)
#     A   B   C
# 0  A0  B0  C0
# 1  A1  B1  C1
# 2  A2  B2  C2
# 3  A3  B3  C3
# 4  A4  B4  C4
# 5  A5  B5  C5
# 6  A6  B6  C6
# 7  A7  B7  C7

# Concatenate df_ver_1, df_origin, and df_ver_2 vertically
df_stack_ver = pd.concat(
    objs = [df_ver_1, df_origin, df_ver_2],
    axis = 0,
    ignore_index = True # Reset index in the concatenated DataFrame
)
print(df_stack_ver)
#       A    B    C
# 0    A4   B4   C4
# 1    A5   B5   C5
# 2    A6   B6   C6
# 3    A7   B7   C7
# 4    A0   B0   C0
# 5    A1   B1   C1
# 6    A2   B2   C2
# 7    A3   B3   C3
# 8    A8   B8   C8
# 9    A9   B9   C9
# 10  A10  B10  C10
# 11  A11  B11  C11

###############################
##    pd.concat(axis = 1)    ##
###############################
''' Concatenate DataFrames horizontally (column-wise) '''

# Original DataFrame
print(df_origin)
#     A   B   C
# 0  A0  B0  C0
# 1  A1  B1  C1
# 2  A2  B2  C2
# 3  A3  B3  C3

# Concatenate df_origin and df_hor_1 horizontally
df_stack_hor = pd.concat(
    objs = [df_origin, df_hor_1],
    axis = 1
)
print(df_stack_hor)
#     A   B   C   D   E   F
# 0  A0  B0  C0  D0  E0  F0
# 1  A1  B1  C1  D1  E1  F1
# 2  A2  B2  C2  D2  E2  F2
# 3  A3  B3  C3  D3  E3  F3

# Concatenate df_hor_1, df_origin, and df_hor_2 horizontally
df_stack_hor = pd.concat(
    objs = [df_hor_1, df_origin, df_hor_2],
    axis = 1
)
print(df_stack_hor)
#     D   E   F   A   B   C   G   H   I
# 0  D0  E0  F0  A0  B0  C0  G0  H0  I0
# 1  D1  E1  F1  A1  B1  C1  G1  H1  I1
# 2  D2  E2  F2  A2  B2  C2  G2  H2  I2
# 3  D3  E3  F3  A3  B3  C3  G3  H3  I3