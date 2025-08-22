'''
Flow of contents:
1. .apply(): Element-wise Function Application
2. .map(): Dictionary Mapping
3. .transform(): Preserving Shape and Multiple Functions application
4. .agg(): Aggregation Functions
5. .groupby(): Grouping Data
6. .filter(): Index-based Filtering
7. .where(): Conditional Filtering and Replacement
8. .combine(): Element-wise Combination
9. .pipe(): Method Chaining with Custom Functions
10. .rolling(): Rolling Window Calculations (short-term trends)
11. .expanding(): Expanding Window Calculations (long-term trends)
12. .ewm(): Exponential Weighted Functions
'''

import pandas as pd
import numpy as np

s_mixed = pd.Series(["apple", "banana", "cherry", 42, 3.14, None])

np.random.seed(42)
s_nums = pd.Series(np.random.normal(loc = 3, scale = 2, size = 5)).round(2)
print(s_nums)
# 0    3.99
# 1    2.72
# 2    4.30
# 3    6.05
# 4    2.53
# dtype: float64

#---------------------------------------------------------------------------------------------------------------#
#----------------------------------------------- 1. .apply() ---------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#

'''
.apply()  method invokes a function on each element or the entire Series.

Key Features:
+ Can apply functions element-wise or to the entire Series
+ Supports both built-in and custom functions
+ Most versatile method for function application
'''

s_applied = s_nums.apply(np.log) # Applying natural logarithm to each element
print(s_applied)
# 0    1.383791
# 1    1.000632
# 2    1.458615
# 3    1.800058
# 4    0.928219
# dtype: float64

s_applied = s_nums.apply(lambda x: 1/(1 + np.exp(-x))) # Apply Sigmoid function
print(s_applied)
# 0    0.981836
# 1    0.938197
# 2    0.986613
# 3    0.997648
# 4    0.926218
# dtype: float64

s_applied = s_mixed.apply(lambda x: str(x).upper() if isinstance(x, str) else x) # Convert strings to uppercase
print(s_applied)
# 0     APPLE
# 1    BANANA
# 2    CHERRY
# 3        42
# 4      3.14
# 5      None
# dtype: object


#---------------------------------------------------------------------------------------------------------------#
#----------------------------------------------- 2. .map() -----------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#

'''
The map() method transforms each element by mapping values using dictionaries, Series, or functions.

Key Features:
+ Optimized for simple transformations and mappings
+ Can use dictionaries, Series, or functions as mapping source
+ Returns NaN for unmapped values when using dict/Series
'''

s_mapped = s_nums.map(np.sin)  # Applying sine function to each element
# print(s_mapped)
# 0   -0.750228
# 1    0.409214
# 2   -0.916166
# 3   -0.231078
# 4    0.574172
# dtype: float64

s_mapped = s_nums.map(lambda x: x**2)  # Squaring each element
print(s_mapped)
# 0    15.9201
# 1     7.3984
# 2    18.4900
# 3    36.6025
# 4     6.4009
# dtype: float64


######################################
## Using a dictionary to map values ##
######################################

s_mapped = s_mixed.map({"apple": "A", "banana": "B", "cherry": "C"})
print(s_mapped)
# 0      A
# 1      B
# 2      C
# 3    NaN
# 4    NaN
# 5    NaN
# dtype: object

'''Unmapped values will be NaN if not found in the mapping dictionary.'''


#---------------------------------------------------------------------------------------------------------------#
#--------------------------------------------- 3. .transform() -------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#

'''
The transform() method applies functions while maintaining the same shape as the input Series.

Key Features:
+ Always returns Series with same length as input
+ Can apply multiple functions simultaneously
+ Useful for normalization and standardization
'''

# Single function transformation
s_transformed = s_nums.transform(lambda x: x+ 1)
print(s_transformed)
# 0    4.99
# 1    3.72
# 2    5.30
# 3    7.05
# 4    3.53
# dtype: float64

# Multiple functions transformation
s_transformed = s_nums.transform(func = {'x+1':lambda x: x+1, 'x*2':lambda x: x*2})
print(s_transformed)
#     x+1    x*2
# 0  4.99   7.98
# 1  3.72   5.44
# 2  5.30   8.60
# 3  7.05  12.10
# 4  3.53   5.06


##################################
## .transform() with .groupby() ##
##################################

df_date_value = pd.DataFrame({
    "Date": [
        "1st", "2nd", "3rd", "4th",
        "1st", "2nd", "3rd", "4th"],
    "Data": [5, 8, 6, 1, 50, 100, 60, 120],
})

print(df_date_value)
#   Date  Data
# 0  1st     5
# 1  2nd     8
# 2  3rd     6
# 3  4th     1
# 4  1st    50
# 5  2nd   100
# 6  3rd    60
# 7  4th   120

# Apply transform with groupby
df_transformed = df_date_value.groupby("Date").transform("sum")
print(df_transformed)
#    Data
# 0    55
# 1   108
# 2    66
# 3   121
# 4    55
# 5   108
# 6    66
# 7   121

'''
The 0-indexed row and the 4-indexed row share the same value (55) because they belong to the same group "1st", and so on.
'''


#---------------------------------------------------------------------------------------------------------------#
#----------------------------------------------- 4. .agg() -----------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#

'''
The agg() method applies aggregation functions to Series or DataFrame, returning a single value or a Series of values.

Key Features:
+ Can apply single or multiple aggregation functions
+ Returns scalar, Series, or DataFrame depending on input
+ Supports both string function names and custom functions
'''

s_agg = s_nums.agg(['mean', 'std', 'min', 'max'])  # Applying multiple aggregation functions
print(s_agg)
# mean    3.918000
# std     1.419355
# min     2.530000
# max     6.050000
# dtype: float64


#########################################
## .agg() with dictionary of functions ##
#########################################

s_agg = s_nums.agg(
    {
        "custom_mean": "mean", 
        "custom_sum": "sum", 
        "custom_range": lambda x: x.max() - x.min()
    }
)

print(s_agg)
# custom_mean      3.918
# custom_sum      19.590
# custom_range     3.520
# dtype: float64


############################
## .agg() with .groupby() ##
############################

df_date_value = pd.DataFrame({
    "Date": [
        "1st", "2nd", "3rd", "4th",
        "1st", "2nd", "3rd", "4th"],
    "Data": [5, 8, 6, 1, 50, 100, 60, 120],
})

print(df_date_value)
#   Date  Data
# 0  1st     5
# 1  2nd     8
# 2  3rd     6
# 3  4th     1
# 4  1st    50
# 5  2nd   100
# 6  3rd    60
# 7  4th   120

'''Apply agg with groupby'''
df_agg = df_date_value.groupby("Date").agg({"Date": "count", "Data": ["mean", "sum"]})
print(df_agg)
#       Date  Data     
#      count  mean  sum
# Date                 
# 1st      2  27.5   55
# 2nd      2  54.0  108
# 3rd      2  33.0   66
# 4th      2  60.5  121

# join the column names for better readability
df_agg.columns = ['_'.join(col).strip() for col in df_agg.columns]
print(df_agg)
#       Date_count  Data_mean  Data_sum
# Date                                 
# 1st            2       27.5        55
# 2nd            2       54.0       108
# 3rd            2       33.0        66
# 4th            2       60.5       121


#---------------------------------------------------------------------------------------------------------------#
#----------------------------------------------- 5. .groupby() -------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#

'''
The groupby() method splits data into groups for separate analysis.

Key Features:
+ Follows split-apply-combine methodology
+ Can group by index levels or external groupers
+ Enables group-wise operations
'''

s_birds_flight = pd.Series(
    data = [390., 350., 30., 20.],
    index = ['Falcon', 'Falcon', 'Parrot', 'Parrot']
)

print(s_birds_flight)
# Falcon    390.0
# Falcon    350.0
# Parrot     30.0
# Parrot     20.0
# dtype: float64


###############################
## Groupping by using level= ##
###############################

s_grouped = s_birds_flight.groupby(level = 0).mean()  # Grouping by the first index level (bird type)
print(s_grouped)
# Falcon    370.0
# Parrot     25.0
# dtype: float64


############################
## Groupping by using by= ##
############################

s_grouped = s_birds_flight.groupby(by = ["a", "b", "a", "b"]).agg(["mean", "max"])
print(s_grouped)
#     mean    max
# a  210.0  390.0
# b  185.0  350.0
# dtype: float64

'''
In this case:
+ Group "a" contains Falcon-390 and Parrot-30, resulting in a mean of 210 and a max of 390.
+ Group "b" contains Falcon-350 and Parrot-20, resulting in a mean of 185 and a max of 350.
'''


#---------------------------------------------------------------------------------------------------------------#
#----------------------------------------------- 6. .filter() --------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#

'''
The filter() method subsets Series based on index labels, not content.

Key Features:
+ Filters based on INDEX LABELS, not values
+ Supports items, like, and regex parameters
+ Cannot be used for content-based filtering
'''

s_birds_flight = pd.Series(
    data = [390., 350., 30., 20., 55],
    index = ['Bird_1', 'Bird_2', 'Bird_3', 'Bird_4', 'Sparrow']
)

#########################
## Filter using items= ##
#########################

s_filtered = s_birds_flight.filter(items = ['Bird_1', 'Bird_2'])  # Filtering by index labels
print(s_filtered)
# Bird_1    390.0
# Bird_2    350.0
# dtype: float64


#########################
## Filter using regex= ##
#########################

s_filtered = s_birds_flight.filter(regex = '[24]$')  # Filtering by index labels ending with '2' or '4'
print(s_filtered)
# Bird_2    350.0
# Bird_4     20.0
# dtype: float64


########################
## Filter using like= ##
########################

s_filtered = s_birds_flight.filter(like = 'rd_')  # Filtering by index labels containing 'Bird'
print(s_filtered)
# Bird_1    390.0
# Bird_2    350.0
# Bird_3     30.0
# Bird_4     20.0
# dtype: float64


#---------------------------------------------------------------------------------------------------------------#
#----------------------------------------------- 7. .where() ---------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#

'''
The where() method replaces values where conditions are False.

Key Features:
+ Keeps original values where condition is True
+ Replaces with specified values where condition is False
+ Supports broadcasting and callable conditions
'''

#################################################
## Using where() and dropna() to filter values ##
#################################################

s_where = s_nums.where(s_nums <= 3)
print(s_where)
# 0     NaN
# 1    2.72
# 2     NaN
# 3     NaN
# 4    2.53
# dtype: float64

s_where = s_nums.where(s_nums <= 3).dropna()
print(s_where)
# 1    2.72
# 4    2.53
# dtype: float64

s_where = s_nums.where(s_nums <= 3).dropna(ignore_index = True)
print(s_where)
# 0    2.72
# 1    2.53
# dtype: float64


#####################################################
## Using where() to replace False-condition values ##
#####################################################

s_where = s_nums.where(s_nums <= 3, other = 0)  # Replacing values greater than 3 with 0
print(s_where)
# 0    0.00
# 1    2.72
# 2    0.00
# 3    0.00
# 4    2.53
# dtype: float64

is_string = is_string = s_mixed.apply(lambda x: isinstance(x, str))
s_where = s_mixed.where(is_string, other = "Unknown")
print(s_where)
# 0      apple
# 1     banana
# 2     cherry
# 3    Unknown
# 4    Unknown
# 5    Unknown
# dtype: object


#---------------------------------------------------------------------------------------------------------------#
#----------------------------------------------- 8. .combine() -------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#

'''
The combine() method combines Series with another Series or scalar using a function.
(works like merging two dataframes)

Key Features:
+ Performs element-wise operations between two Series
+ Handles missing values with fill_value parameter
+ Can combine with scalars or other Series
'''

s1 = pd.Series({'falcon': 330.0, 'eagle': 160.0})
s2 = pd.Series({'falcon': 345.0, 'eagle': 200.0, 'duck': 30.0})

#########################################
## Basic combine with other= and func= ##
#########################################

s_combined = s1.combine(other = s2, func = max)
print(s_combined)
# duck        NaN
# eagle     200.0
# falcon    345.0
# dtype: float64

'''MUST always specify the func= parameter, otherwise it will raise an error.'''


############################################
## Combine with fill_value= to handle NaN ##
############################################

s_combined = s1.combine(other = s2, func = max, fill_value = 0)
print(s_combined)
# duck       30.0
# eagle     200.0
# falcon    345.0
# dtype: float64

'''
In this case, since s1 does not have a value for 'duck', 
it is filled with 0.

Therefore, the max function compares 0 with 30.0,
resulting in 'duck' having a value of 30.0.
'''


#----------------------------------------------------------------------------------------------------------------#
#----------------------------------------------- 9. .pipe() -----------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------#

'''
The pipe() method enables method chaining by applying functions that expect Series or DataFrames.

Key Features:
+ Facilitates readable method chaining
+ Can pass additional arguments to functions
+ Supports tuple syntax for functions expecting data as non-first argument
'''

import scipy as sp

################################
## Handle quantitative series ##
################################

np.random.seed(42)

query = (
    pd.Series(np.random.normal(loc = 3, scale = 2, size = 30))
    .round(2)
    .pipe(lambda ser: ser[ser < 2.9])
    .pipe(lambda ser: sp.stats.shapiro(ser))
)

print(query)
# ShapiroResult(statistic=np.float64(0.8865328120075993), pvalue=np.float64(0.033671906069434675))


###############################
## Handle categorical series ##
###############################

s_gender = pd.Series(["F", "LGBTQ", "M", "F", "M", "LGBTQ", "F", "M", "F", "M", "M", "LGBTQ"])

query = (
    s_gender.copy()
    .value_counts()
    .pipe(lambda ser: ser/ser.sum() * 100)  # Calculate percentage
    .round(2) # Round to 2 decimal places
    .pipe(lambda ser: ser.astype(str) + "%")   # Convert to string with percentage sign
)

print(query)
# M        41.67%
# F        33.33%
# LGBTQ     25.0%
# Name: count, dtype: object


#---------------------------------------------------------------------------------------------------------------#
#----------------------------------------------- 10. .rolling() ------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#

'''
The .rolling() method creates a fixed-size moving window that slides through your data. 

It calculates statistics over a consistent number of observations

Key Parameters:
+ window: Size of the moving window (required)
+ min_periods: Minimum observations needed for a value (defaults to window size)
+ center: If True, labels are set at the center of the window
+ win_type: Specifies window type for weighted calculations
'''

###############
## Basic use ##
###############

print(s_nums)
# 0    3.99
# 1    2.72
# 2    4.30
# 3    6.05
# 4    2.53
# dtype: float64

s_rolling = s_nums.rolling(window = 2).mean()  # Calculate rolling mean with a window of 2
print(s_rolling)
# 0      NaN (mean of [NaN, 0-indexed])
# 1    3.355 (mean of [0-indexed, 1-indexed])
# 2    3.510 (mean of [1-indexed, 2-indexed])
# 3    5.175 
# 4    4.290
# dtype: float64

s_rolling = s_nums.rolling(window = 3).mean()  # Calculate rolling mean with a window of 3
print(s_rolling)
# 0         NaN (mean of [NaN, NaN, 1-indexed])
# 1         NaN (mean of [NaN, 0-indexed, 1-indexed])
# 2    3.670000 (mean of [0-indexed, 1-indexed, 2-indexed])
# 3    4.356667
# 4    4.293333
# dtype: float64


###################################
## Rolling with time-based index ##
###################################

s_nums_time = pd.Series(
    data = s_nums.values,
    index = [pd.Timestamp('20130101 09:00:00'),
             pd.Timestamp('20130101 09:00:02'),
             pd.Timestamp('20130101 09:00:03'),
             pd.Timestamp('20130101 09:00:05'),
             pd.Timestamp('20130101 09:00:06')]
)

s_rolling = s_nums_time.rolling(window = '2s').mean()  # Calculate rolling mean with a 2-second window
# for each timestamp t, 
# take all observations whose timestamps fall in the interval (t − 2 seconds, t], 
# then compute the mean.

print(s_rolling)                                       
# 2013-01-01 09:00:00    3.99
# 2013-01-01 09:00:02    2.72
# 2013-01-01 09:00:03    3.51
# 2013-01-01 09:00:05    6.05
# 2013-01-01 09:00:06    4.29
# dtype: float64

'''
3.99:
 + 2013-01-01 09:00:00 (window: (08:59:58, 09:00:00])
 + Included points: only 09:00:00 → 3.99
 + => Mean = 3.99

2.72:
 + 2013-01-01 09:00:02 (window: (09:00:00, 09:00:02])
 + Included points: only 09:00:02 → 2.72
 + => Mean = 2.72

3.51:
 + 2013-01-01 09:00:03 (window: (09:00:01, 09:00:03])
 + Included points: 09:00:02 (2.72) and 09:00:03 (4.30)
 + => Mean = (2.72 + 4.30) / 2 = 3.51
'''


#---------------------------------------------------------------------------------------------------------------#
#----------------------------------------------- 11. .expanding() ----------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#

'''
The .expanding() method creates a growing window that starts from the first observation 
and includes all data up to the current point. 

This produces cumulative statistics ideal for long-term trend analysis.

Key Parameters:
+ min_periods: Minimum observations required (default is 1)
+ center: Sets window label positioning
'''

###############
## Basic use ##
###############

print(s_nums)
# 0    3.99
# 1    2.72
# 2    4.30
# 3    6.05
# 4    2.53
# dtype: float64

s_expanding = s_nums.expanding().mean()  # Calculate expanding mean
print(s_expanding)
# 0    3.990 (mean of [0-indexed])
# 1    3.355 (mean of [0-indexed, 1-indexed])
# 2    3.670 (mean of [0-indexed, 1-indexed, 2-indexed])
# 3    4.265
# 4    3.918
# dtype: float64

s_expanding = s_nums.expanding().sum()  # Calculate expanding sum (like cumulative sum)
print(s_expanding)
# 0     3.99 (sum of [0-indexed])
# 1     6.71 (sum of [0-indexed, 1-indexed])
# 2    11.01 (sum of [0-indexed, 1-indexed, 2-indexed])
# 3    17.06
# 4    19.59
# dtype: float64


#############################
## Using with min_periods= ##
#############################

s_expanding = s_nums.expanding(min_periods = 3).mean()  # Calculate expanding mean with minimum 3 observations
print(s_expanding)
# 0      NaN (not enough 3 observations)
# 1      NaN (not enough 3 observations)
# 2    3.670 (mean of [0-indexed, 1-indexed, 2-indexed])
# 3    4.265 (mean of [0-indexed, 1-indexed, 2-indexed, 3-indexed])
# 4    3.918
# dtype: float64


#---------------------------------------------------------------------------------------------------------------#
#----------------------------------------------- 12. .ewm() ----------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------#

'''
The .ewm() method applies exponentially decreasing weights to observations, 
giving more importance to recent data while still considering historical values. 

This method is particularly valuable in financial analysis and forecasting.

Weighting Parameters (exactly one required):
+ span: Decay in terms of span, α = 2/(span+1)
+ halflife: Decay in terms of half-life
+ alpha: Direct smoothing factor (0 < α ≤ 1)
+ com: Center of mass, α = 1/(1+com)

Additional Parameters:
+ adjust: Controls weighting calculation method
+ min_periods: Minimum observations needed
'''

s_ewm = s_nums.ewm(span = 2).mean()  # Calculate exponentially weighted moving average with span of 2
print(s_ewm)
# 0    3.990000
# 1    3.037500
# 2    3.911538
# 3    5.355000
# 4    3.463884
# dtype: float64

'''
EXPLANATION:

-------------
1) Smoothing factor from span

alpha = 2 / (span + 1)
      = 2 / (2 + 1)
      = 2 / 3
      ≈ 0.6666667

one_minus_alpha = 1 - 2/3 = 1/3

-------------
2) Meaning of adjust=True (the default)

EWMA_t is a normalized weighted average over all observations up to t,
with geometrically decaying weights proportional to:
   [1, (1-alpha), (1-alpha)^2, ..., (1-alpha)^t]

So:
   EWMA_t = sum( (1-alpha)^k * x_{t-k} for k=0..t ) / sum( (1-alpha)^k for k=0..t )

-------------
3) Step-by-step verification on the given data

x0, x1, x2, x3, x4 = 3.99, 2.72, 4.30, 6.05, 2.53

t = 0
# weights: [1]
# EWMA_0 = 3.99
# ewma_0 = 3.99  # -> 3.990000

t = 1
# weights: [1 (for x1), 1/3 (for x0)]
# weighted sum = 1*2.72 + (1/3)*3.99 = 2.72 + 1.33 = 4.05
# sum weights = 1 + 1/3 = 4/3
# ewma_1 = 4.05 / (4/3) = 3.0375

t = 2
# weights: [1, 1/3, 1/9]
# weighted sum = 1*4.30 + (1/3)*2.72 + (1/9)*3.99
#              = 4.30 + 0.906666... + 0.443333... = 5.65
# sum weights = 1 + 1/3 + 1/9 = 13/9 ≈ 1.444444...
# ewma_2 = 5.65 / (13/9) = 3.911538...

t = 3
# weights: [1, 1/3, 1/9, 1/27]
# weighted sum = 6.05 + 1.433333... + 0.302222... + 0.147777... = 7.933333...
# sum weights = 1 + 1/3 + 1/9 + 1/27 = 40/27 ≈ 1.481481...
# ewma_3 = 7.933333... / (40/27) = 5.355000

t = 4
# weights: [1, 1/3, 1/9, 1/27, 1/81]
# weighted sum = 2.53 + 2.016666... + 0.477777... + 0.100740... + 0.049259... = 5.174444...
# sum weights = 1 + 1/3 + 1/9 + 1/27 + 1/81 = 121/81 ≈ 1.493827...
# ewma_4 = 5.174444... / (121/81) = 3.463884...

-----------------
4) Key takeaways
- span=2 implies alpha=2/3, putting strong weight on the newest observation.
- adjust=True computes a normalized weighted mean across all past points.
- Weights decay by a factor of 1/3 for each step further into the past.

-----------------
5) Recursive form (for intuition)

If adjust=False, pandas uses the recursive update exactly:
  EWMA_t = alpha * x_t + (1 - alpha) * EWMA_{t-1}

with EWMA_0 = x_0.
'''