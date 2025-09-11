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


#---------------------------------------------------------------------------------------------------------#
#------------------------------------ 1. pd.plotting.scatter_matrix() ------------------------------------#
#---------------------------------------------------------------------------------------------------------#
'''
Creates a matrix of scatter plots for visualizing relationships between multiple

# frame: DataFrame to plot
# alpha: Transparency level (0.0-1.0, default 0.5)
# figsize: Figure size as (width, height) tuple
# diagonal: 'hist' or 'kde' for diagonal plots
# marker: Matplotlib marker style (default '.')
# range_padding: Axis range padding (default 0.05)
'''

#######################
## diagonal = "hist" ##
#######################

pd.plotting.scatter_matrix(
    frame = df_pokemon.select_dtypes(include="number").drop(columns="Total"),
    alpha = 0.5,
    figsize = (10, 10),
    diagonal = "hist",
    marker = "x",
    grid = True,
    hist_kwds = {"bins": 20, "color": "gray"},
    range_padding = 0.1
)
plt.title("Scatter Matrix with Histograms on Diagonal")
plt.show()

######################
## diagonal = "kde" ##
######################

pd.plotting.scatter_matrix(
    frame = df_pokemon.select_dtypes(include="number").drop(columns="Total"),
    alpha = 0.5,
    figsize = (10, 10),
    diagonal = "kde",
    marker = "o",
    grid = True,
    hist_kwds = {"bins": 20, "color": "gray"},
    density_kwds = {"color": "gray"},
    range_padding = 0.1
)
plt.title("Scatter Matrix with KDE on Diagonal")
plt.show()


#---------------------------------------------------------------------------------------------------------#
#------------------------------ 2. pd.plotting.andrews_curves() ------------------------------------------#
#---------------------------------------------------------------------------------------------------------#
'''
Visualizes multivariate data by mapping each observation to a function using Fourier series transformation

# frame: DataFrame with data to plot
# class_column: Column name containing class labels
# samples: Number of points per curve (default 200)
# color: Colors for different classes
# colormap: Matplotlib colormap
'''

pd.plotting.andrews_curves(
    frame = df_pokemon[["Attack", "Defense", "Type_1"]],
    class_column = "Type_1",
    samples = 200,
    colormap = "tab20",
    alpha = 0.5,
    linewidth = 1
)
plt.title("Andrews Curves of Pokémon by Type 1")
plt.show()


#---------------------------------------------------------------------------------------------------------#
#--------------------------------- 3. pd.plotting.parallel_coordinates() ---------------------------------#
#---------------------------------------------------------------------------------------------------------#
'''
Creates parallel coordinate plots for multivariate data visualization 
where each vertical axis represents a variable.

# frame: DataFrame to plot
# class_column: Column containing class names
# cols: List of columns to include (optional)
# color: Colors for different classes
# use_columns: Use columns as x-tick labels
# colormap: Colormap for line colors
# axvlines: Add vertical lines at each variable (default True)
# sort_labels: Sort class labels (default False)
'''

pd.plotting.parallel_coordinates(
    frame = df_pokemon[["Attack", "Defense", "Legendary"]],
    class_column = "Type_1",
    color = ("#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"),
    colormap = "tab10",
    axvlines = True,
    sort_labels = True,
    alpha = 0.5,
    linewidth = 1
)
plt.title("Parallel Coordinates Plot of Pokémon by Type 1")
plt.show()