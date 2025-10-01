'''
1. pivot_wider: dr.pivot_wider()
2. pivot_longer: dr.pivot_longer()
3. crosstab: dr.table()
'''

import datar.all as dr
from datar import f
import pandas as pd
import numpy as np

# Suppress all warnings
import warnings
warnings.filterwarnings("ignore")


#---------------------------------------------------------------------------------------------------------#
#------------------------------------------ 1. dr.pivot_wider() ------------------------------------------#
#---------------------------------------------------------------------------------------------------------#

########################
## Create sample data ##
########################

'''
The dr.pivot_wider() converts unique values from one column into multiple columns in the DataFrame.
=> Results in a wider DataFrame than the original.

NOTE: if the chosen "index" column has duplicates => RAISE ERROR
'''

dates = pd.date_range('2024-01-01', periods=30) # 30 days
regions   = ['North', 'South', 'East', 'West']
products  = ['Widget', 'Gadget', 'Doohickey']

np.random.seed(42)
df_sales = pd.DataFrame(
    {   'ID'        : range(1, 201),
        'date'      : np.random.choice(dates, size=200),
        'region'    : np.random.choice(regions, size=200),
        'product'   : np.random.choice(products, size=200),
        'quantity'  : np.random.randint(1, 20, size=200),
        'unit_price': np.round(np.random.uniform(5, 50, size=200), 2)
    }
).assign(sales = lambda df: df.eval("quantity * unit_price")) # Add a column with the total sales amount

df_sales.head()
#    ID       date region    product  quantity  unit_price   sales
# 0   1 2024-01-07   East     Gadget         5        6.19   30.95
# 1   2 2024-01-20  North     Widget        10       21.94  219.40
# 2   3 2024-01-29   East  Doohickey         5       41.47  207.35
# 3   4 2024-01-15   East     Widget         4       49.43  197.72
# 4   5 2024-01-11  North     Widget         2       11.77   23.54

##################################
## dr.pivot_wider() basic usage ##
##################################

print(
    df_sales >> 
    dr.pivot_wider(
        names_from = f.region, 
        values_from = f.sales
    )
)

