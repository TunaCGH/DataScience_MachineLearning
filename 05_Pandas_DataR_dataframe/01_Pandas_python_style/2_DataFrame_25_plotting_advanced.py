'''
pandas.plotting offers several advanced plotting functions that can be used to visualize data in a DataFrame. 

##################################

1. pd.plotting.scatter_matrix()

2. pd.plotting.andrews_curves()

3. pd.plotting.parallel_coordinates()

4. pd.plotting.radviz()

5. pd.plotting.lag_plot()

6. pd.plotting.autocorrelation_plot()

7. pd.plotting.bootstrap_plot()

8. pd.plotting.boxplot()

9. pd.plotting.table()

10. pd.plotting.register_matplotlib_converters()

11. pd.plotting.deregister_matplotlib_converters()
'''

import pandas as pd
import matplotlib.pyplot as plt

# General DataFrame
df_pokemon = (
    pd.read_csv(
        filepath_or_buffer = "05_Pandas_DataR_dataframe/data/pokemon.csv",
        dtype = {
            "Type 1": "category",
            "Type 2": "category",
            "Generation": "category",
            "Legendary": "bool"
        }
    )
    .drop(columns = ["#"])
    .pipe(lambda df: df.set_axis(df.columns.str.strip().str.replace(r"\s+", "_", regex = True).str.replace(".", ""), axis=1))
    .assign(Generation = lambda df: df['Generation'].cat.as_ordered())
)

# Time series DataFrame
df_aq = (
    pd.read_csv("05_Pandas_DataR_dataframe/data/air_quality_no2_long.csv")
    .rename(columns={"date.utc": "date"})
    .assign(date = lambda df: pd.to_datetime(df["date"], format="%Y-%m-%d %H:%M:%S%z"))
)