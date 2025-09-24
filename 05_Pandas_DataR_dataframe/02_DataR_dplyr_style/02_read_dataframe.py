'''
To read dataframe, just use pandas.read.....() functions, then convert to datar tibble if needed.
'''

from datar.all import *
import pandas as pd

# Suppress specific warnings from pipda
import warnings
from pipda.utils import PipeableCallCheckWarning
warnings.filterwarnings("ignore", category=PipeableCallCheckWarning)

#--------------------------------------------------------------------------------------------------------------------#
#------------------------------------- Read dataframe using pandas.read...() ----------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

tb_csv = tibble(pd.read_csv('05_Pandas_DataR_dataframe/data/air_quality_no2_long.csv'))
print(tb_csv.head())
#       city  country                   date.utc location parameter     value     unit
#   <object> <object>                   <object> <object>  <object> <float64> <object>
# 0    Paris       FR  2019-06-21 00:00:00+00:00  FR04014       no2      20.0    µg/m³
# 1    Paris       FR  2019-06-20 23:00:00+00:00  FR04014       no2      21.8    µg/m³
# 2    Paris       FR  2019-06-20 22:00:00+00:00  FR04014       no2      26.5    µg/m³
# 3    Paris       FR  2019-06-20 21:00:00+00:00  FR04014       no2      24.9    µg/m³
# 4    Paris       FR  2019-06-20 20:00:00+00:00  FR04014       no2      21.4    µg/m³

tb_excel = tibble(pd.read_excel("05_Pandas_DataR_dataframe/data/emp_sheetname.xlsx", sheet_name='emp'))
print(tb_excel)
#         id      name    salary       start_date        dept
#   <object>  <object> <float64> <datetime64[ns]>    <object>
# 0        1      Rick    623.30       2012-01-01          IT
# 1        2       Dan    515.20       2013-09-23  Operations
# 2        3  Michelle    611.00       2014-11-15          IT
# 3        4      Ryan    729.00       2014-05-11          HR
# 4               Gary    843.25       2015-03-27     Finance
# 5        6      Nina    578.00       2013-05-21          IT
# 6        7     Simon    632.80       2013-07-30  Operations
# 7        8      Guru    722.50       2014-06-17     Finance