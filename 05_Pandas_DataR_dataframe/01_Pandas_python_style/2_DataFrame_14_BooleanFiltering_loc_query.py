'''
Boolean Filtering or Boolean Indexing is a powerful technique in Pandas 
that allows you to filter data based on specific conditions. 

###############################

1. Single Condition Examples:
   + Logic Operators: >, <, >=, <=, .between(), ==, !=
   + .isin()
   + String Boolean: .str.contains(), .str.startswith(), .str.endswith(), ....
   + DateTime Boolean: .dt.is_month_start, .dt.is_month_end, ...

2. Negation of Condition: ~ (tilde) operator

3. Combine Multiple Conditions:
   + & (and),
   + | (or)
   + Combine & and |

4. Using .loc[] for Boolean Filtering within specific columns

5. Using .query() method for short-syntax condition filtering
'''

import pandas as pd
import re

df_pokemon = (
    pd.read_csv(
        filepath_or_buffer = "05_Pandas_DataR_dataframe/data/pokemon.csv",
        index_col = "#",
        dtype = {
            "Type 1": "category",
            "Type 2": "category",
            "Generation": "category",
            "Legendary": "bool"
        }
    )
    .rename(columns = lambda col: re.sub(r"\s+", "_", col.strip().replace(".", "")))
    .assign(Generation = lambda df: df['Generation'].cat.as_ordered())
)

print(df_pokemon.head())
#                     Name Type_1  Type_2  Total  HP  Attack  Defense  Sp_Atk  Sp_Def  Speed Generation  Legendary
# #                                                                                                               
# 1              Bulbasaur  Grass  Poison    318  45      49       49      65      65     45          1      False
# 2                Ivysaur  Grass  Poison    405  60      62       63      80      80     60          1      False
# 3               Venusaur  Grass  Poison    525  80      82       83     100     100     80          1      False
# 3  VenusaurMega Venusaur  Grass  Poison    625  80     100      123     122     120     80          1      False
# 4             Charmander   Fire     NaN    309  39      52       43      60      50     65          1      False

print(df_pokemon.dtypes)
# Index: 800 entries, 1 to 721
# Data columns (total 12 columns):
#  #   Column      Non-Null Count  Dtype   
# ---  ------      --------------  -----   
#  0   Name        800 non-null    object  
#  1   Type_1      800 non-null    category
#  2   Type_2      414 non-null    category
#  3   Total       800 non-null    int64   
#  4   HP          800 non-null    int64   
#  5   Attack      800 non-null    int64   
#  6   Defense     800 non-null    int64   
#  7   Sp_Atk      800 non-null    int64   
#  8   Sp_Def      800 non-null    int64   
#  9   Speed       800 non-null    int64   
#  10  Generation  800 non-null    category
#  11  Legendary   800 non-null    bool    
# dtypes: bool(1), category(3), int64(7), object(1)
# memory usage: 60.8+ KB

print(df_pokemon['Generation'].cat.categories)
# Name: Generation, Length: 800, dtype: category
# Categories (6, object): ['1' < '2' < '3' < '4' < '5' < '6']