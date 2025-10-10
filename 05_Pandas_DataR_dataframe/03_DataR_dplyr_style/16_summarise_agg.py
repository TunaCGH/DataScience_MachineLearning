'''
dr.summarise() is a transformation that aggregates data,
by using aggregation functions like sum, mean, min, max, etc.

############

dr.summarise() with single column

dr.summarise() with multiple columns
 + Different aggregation functions
 + Same aggregation function (dr.across())
 + Same aggregation function with dr.where() (dr.across(dr.where()))
'''

import datar.all as dr
from datar import f
import pandas as pd
import numpy as np

# Suppress all warnings
import warnings
warnings.filterwarnings("ignore")

########################

tb_pokemon = dr.tibble(
    pd.read_csv(
        filepath_or_buffer = "05_Pandas_DataR_dataframe/data/pokemon.csv",
        index_col = "#",
        dtype = {"Legendary": "bool"}
    )
    .pipe(lambda df: df.set_axis(df.columns.str.strip().str.replace(r"\s+", "_", regex = True).str.replace(".", ""), axis=1))
    >> dr.mutate(
        dr.across(
            dr.where(dr.is_character) | f.Type_2 | f.Generation, # Convert to categorical (factor)
            dr.as_factor
        )
    )
)

print(
    tb_pokemon
    >> dr.slice_head(n=5)
)
#                     Name     Type_1     Type_2   Total      HP  Attack  Defense  Sp_Atk  Sp_Def   Speed Generation  Legendary
                                                                                                                             
# #             <category> <category> <category> <int64> <int64> <int64>  <int64> <int64> <int64> <int64> <category>     <bool>
# 1              Bulbasaur      Grass     Poison     318      45      49       49      65      65      45          1      False
# 2                Ivysaur      Grass     Poison     405      60      62       63      80      80      60          1      False
# 3               Venusaur      Grass     Poison     525      80      82       83     100     100      80          1      False
# 3  VenusaurMega Venusaur      Grass     Poison     625      80     100      123     122     120      80          1      False
# 4             Charmander       Fire        NaN     309      39      52       43      60      50      65          1      False


##########################################
##       Summarise single column        ##
##########################################

print(
    tb_pokemon
    >> dr.summarise(
        avg_hp = dr.mean(f.HP)
    )
)
#      avg_hp
#   <float64>
# 0  69.25875

###########################################
##        Summarise multiple cols        ##
###########################################

#--------
## Different agg func
#--------

print(
    tb_pokemon
    >> dr.summarise(
        avg_hp = dr.mean(f.HP),
        max_def = np.max(f.Defense),
        min_atk = dr.min_(f.Attack), # dr.min_() to avoid conflict with Python built-in min()
        total_spd = np.sum(f.Speed)
    )
)
#      avg_hp  max_def  min_atk  total_spd
#   <float64>  <int64>  <int64>    <int64>
# 0  69.25875      230        5      54622

#--------
## Same agg func (dr.across())
#--------

print(
    tb_pokemon
    >> dr.summarise(
        dr.across(
            f.HP | f.Attack | f.Defense | f.Sp_Atk | f.Sp_Def | f.Speed,
            dr.mean,
            _names = "avg_{_col}" # _col is a placeholder for the original column name
        )
    )
)
#      avg_HP  avg_Attack  avg_Defense  avg_Sp_Atk  avg_Sp_Def  avg_Speed
#   <float64>   <float64>    <float64>   <float64>   <float64>  <float64>
# 0  69.25875    79.00125      73.8425       72.82     71.9025    68.2775

#--------
## Same agg func (dr.across(dr.where()))
#--------

print(
    tb_pokemon
    >> dr.summarise(
        dr.across(
            dr.where(dr.is_numeric) & ~f.Legendary, # All numeric columns except 'Legendary'
            lambda col: np.quantile(col, [0.25, 0.5, 0.75]),
            _names = "quantile_{_col}" # _col is a placeholder for the original column name
        )
    )
    >> dr.mutate(id = ["Q1", "Median", "Q3"]) # Add an id column for the quantiles
    >> dr.column_to_rownames("id") # Set the id column as row names
)
#         quantile_Total  quantile_HP  quantile_Attack  quantile_Defense  quantile_Sp_Atk  quantile_Sp_Def  quantile_Speed
#              <float64>    <float64>        <float64>         <float64>        <float64>        <float64>       <float64>
# Q1               330.0         50.0             55.0              50.0            49.75             50.0            45.0
# Median           450.0         65.0             75.0              70.0            65.00             70.0            65.0
# Q3               515.0         80.0            100.0              90.0            95.00             90.0            90.0