'''
1. dr.slice_(): allows selecting rows by their positions (indices).

2. dr.slice_min(): allows selecting rows with the smallest values in a specified column.

3. dr.slice_max(): allows selecting rows with the largest values in a specified column.
'''

import datar.all as dr
from datar import f

import pandas as pd

# Suppress all warnings
import warnings
warnings.filterwarnings("ignore")

########################

df_baseball = pd.read_csv(
    filepath_or_buffer = "05_Pandas_DataR_dataframe/data/baseball.csv",
    dtype = {
        "Team": "category",
        "Position": "category",
        "PosCategory": "category"
    }
)

print(df_baseball.head())
#               Name       Team       Position  Height  Weight       Age PosCategory
#           <object> <category>     <category> <int64> <int64> <float64>  <category>
# 0    Adam_Donachie        BAL        Catcher      74     180     22.99     Catcher
# 1        Paul_Bako        BAL        Catcher      74     215     34.69     Catcher
# 2  Ramon_Hernandez        BAL        Catcher      72     210     30.78     Catcher
# 3     Kevin_Millar        BAL  First_Baseman      72     210     35.43   Infielder
# 4      Chris_Gomez        BAL  First_Baseman      73     188     35.71   Infielder


#------------------------------------------------------------------------------------------------------------#
#------------------------------------------ 1. dr.slice_(...) -----------------------------------------------#
#------------------------------------------------------------------------------------------------------------#