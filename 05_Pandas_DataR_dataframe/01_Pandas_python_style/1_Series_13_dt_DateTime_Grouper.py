'''
The pandas.Series.dt accessor is a powerful interface 
that provides access to datetime-like properties and methods for pandas Series.

Supported Types: datetime64[ns], datetime64[ns, tz], Period, timedelta[ns]

Flow of contents:
0. Creating datetime data and index:
    + Datetime data: pd.to_datetime(), astype('datetime64[ns]'), pd.date_range(), pd.bdate_range()
    + Timedelta data: pd.to_timedelta(), astype('timedelta64[ns]'), pd.timedelta_range()
    + Period: pd.Period(), .Series.to_period(), pd.period_range(), 
    + pd.infer_freq(): Infers the frequency of a DatetimeIndex

1. Basic properties:
    + .dt.year, .dt.month, .dt.day
    + .dt.hour, .dt.minute, .dt.second
    + .dt.microsecond, .dt.nanosecond

2. ISO Calendar properties:
    + .dt.isocalendar(): Returns a DataFrame with ISO components = year + week + day
    + .dt.isocalendar().year: ISO year
    + .dt.isocalendar().week: ISO week number (1-53)
    + .dt.isocalendar().day: ISO day of the week (1=Monday, 7=Sunday)

3. Extended properties:
    + .dt.dayofyear
    + .dt.dayofweek, .dt.weekday
    + .dt.quarter
    + .dt.days_in_month

4. Boolean properties:
    + .dt.is_month_start, .dt.is_month_end
    + .dt.is_quarter_start, .dt.is_quarter_end
    + .dt.is_year_start, .dt.is_year_end
    + .dt.is_leap_year

5. Extract Python datetime objects:
    + .dt.date: Returns datetime.date objects (date only)
    + .dt.time: Returns datetime.time objects (time only)
    + .dt.timetz: Returns datetime.time with timezone information

6. String Representation Methods:
    + .dt.strftime(format): Custom string formatting using strftime codes
    + .dt.day_name(): Return day names ("Monday", "Tuesday", etc.)
    + .dt.month_name(): Return month names ("January", "February", etc.)

7. Time Rounding Methods:
    + .dt.round(freq): Round to nearest specified frequency
    + .dt.floor(freq): Round down to specified frequency
    + .dt.ceil(freq): Round up to specified frequency
    + .dt.normalize(): Convert times to midnight (00:00:00)

8. Timezone Handling:
    + .dt.tz: Get current timezone information
    + .dt.tz_localize(tz): Assign timezone to naive datetime
    + .dt.tz_convert(tz):  Convert between timezones

9. Timedelta Handling:
    + .dt.components: Returns DataFrame with timedelta components (days, hours, minutes, etc.)
    + .dt.days: Days component
    + .dt.seconds: Seconds component (0-86399)
    + .dt.total_seconds(): Total duration in seconds

10. Grouper with datetime-like data:
    + pd.Grouper(key=None, level=None, freq=None, axis=0, sort=False, closed=None, label=None, convention='start', base=0, origin='start', offset=None)
    + Used in groupby operations to group by specific time periods (e.g., month, year)
'''

###################################

'''
COMMON FREQUENCY CODES:

'ns' - Nanosecond
'us' - Microsecond
'ms' - Millisecond
's' - Second

'min' - Minute
'h' - Hour

'D' - Day
'B' - Business day
'W' - Weekly

'ME' - Month end
'MS' - Month start

'QE' - Quarter end
'QS' - Quarter start

'YE' - Year end
'YS' - Year start
'''

import pandas as pd
import numpy as np

#-------------------------------------------------------------------------------------------------------------#
#------------------------------------ 0. Creating datetime data and index ------------------------------------#
#-------------------------------------------------------------------------------------------------------------#
'''
0. Creating a Series with datetime data:
    + Timedelta data: pd.to_timedelta(), astype('timedelta64[ns]'), pd.timedelta_range()
    + Period: pd.period(), .Series.to_period(), pd.period_range(), 
    + pd.infer_freq(): Infers the frequency of a DatetimeIndex
'''

'''
#--------------------------
## Datetime data
#--------------------------
'''

s_original = pd.Series(['2023-01-01', '2023-02-15', '2023-03-20'])
print(s_original.dtypes) # object

s_dayfirst = pd.Series(['31/12/2023', '15/11/2023', '20/10/2023'])
print(s_dayfirst.dtypes) # object

######################
## pd.to_datetime() ##
######################

# Basic use
s_datetime = pd.to_datetime(s_original)
print(s_datetime)
# 0   2023-01-01
# 1   2023-02-15
# 2   2023-03-20
# dtype: datetime64[ns]

# Set the "dayfirst = True" for string format "DD/MM/YYYY" (or something similar like DD-MM-YYYY, DD.MM.YYYY)
s_datetime = pd.to_datetime(arg = s_dayfirst, dayfirst = True)
print(s_datetime)
# 0   2023-12-31
# 1   2023-11-15
# 2   2023-10-20
# dtype: datetime64[ns]

##############################
## astype('datetime64[ns]') ##
##############################

s_datetime = s_original.astype('datetime64[ns]')
print(s_datetime)
# 0   2023-01-01
# 1   2023-02-15
# 2   2023-03-20
# dtype: datetime64[ns]

s_datetime = s_dayfirst.astype('datetime64[ns]')
print(s_datetime)
# 0   2023-12-31
# 1   2023-11-15
# 2   2023-10-20
# dtype: datetime64[ns]

#####################
## pd.date_range() ##
#####################

# Create a DatetimeIndex with a specified frequency
# Can use this DatetimeIndex as index for a Series or DataFrame
# https://pandas.pydata.org/docs/reference/api/pandas.date_range.html

# Create a date range from '2023-01-01' to '2023-01-10' with daily frequency
date_rng = pd.date_range(start = '2023-01-01', end = '2023-01-10', freq = 'D')
print(date_rng)
# DatetimeIndex(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04',
#                '2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08',
#                '2023-01-09', '2023-01-10'],
#               dtype='datetime64[ns]', freq='D')

np.random.seed(0)
s_daterange = pd.Series(data = np.random.randint(0, 100, size = len(date_rng)), index = date_rng)
print(s_daterange)
# 2023-01-01    44
# 2023-01-02    47
# 2023-01-03    64
# 2023-01-04    67
# 2023-01-05    67
# 2023-01-06     9
# 2023-01-07    83
# 2023-01-08    21
# 2023-01-09    36
# 2023-01-10    87
# Freq: D, dtype: int64

######################
## pd.bdate_range() ##
######################

# Works like pd.date_range() but only includes business days (Monday to Friday)
# https://pandas.pydata.org/docs/reference/api/pandas.bdate_range.html

bdate_range = pd.bdate_range(start = '2023-01-01', end = '2023-01-10', freq = 'B') # 'B' means business day frequency

print(bdate_range)
# DatetimeIndex(['2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05',
#                '2023-01-06', '2023-01-09', '2023-01-10'],
#               dtype='datetime64[ns]', freq='B')


# (Here, the weekends 2023-01-01, 2023-01-07, and 2023-01-08 are excluded 
# because they are not business days)


'''
#--------------------------
## Timedelta data
#--------------------------
'''

s_original = pd.Series(['1 days', '2 days 03:00:00', '4 days 05:30:00'])
s_original_nums = pd.Series([1, 2.5, 4.25])

#######################
## pd.to_timedelta() ##
#######################

# Basic use
s_timedelta = pd.to_timedelta(s_original)
print(s_timedelta)
# 0   1 days 00:00:00
# 1   2 days 03:00:00
# 2   4 days 05:30:00
# dtype: timedelta64[ns]

# Specify the unit of the numeric input
s_timedelta = pd.to_timedelta(s_original_nums, unit = 'h') # 'h' means hours
print(s_timedelta)
# 0   0 days 01:00:00 (1 -> 1 hour)
# 1   0 days 02:30:00 (2.5 -> 2 hours 30 minutes)
# 2   0 days 04:15:00 (4.25 -> 4 hours 15 minutes)
# dtype: timedelta64[ns]

'''
Only specify "unit=" when the input is NUMERIC (not string or object).
'''

###############################
## astype('timedelta64[ns]') ##
###############################

s_timedelta = s_original.astype('timedelta64[ns]')
print(s_timedelta)
# 0   1 days 00:00:00
# 1   2 days 03:00:00
# 2   4 days 05:30:00
# dtype: timedelta64[ns]

s_timedelta = s_original_nums.astype('timedelta64[ns]') # Interpreted as nanoseconds
print(s_timedelta)
# 0   0 days 00:00:00.000000001
# 1   0 days 00:00:00.000000002
# 2   0 days 00:00:00.000000004
# dtype: timedelta64[ns]

s_timedelta = s_original_nums.astype('timedelta64[h]') # Interpreted as hours
print(s_timedelta)
# 0   0 days 01:00:00
# 1   0 days 02:00:00
# 2   0 days 04:00:00
# dtype: timedelta64[s]

##########################
## pd.timedelta_range() ##
##########################
# Create a TimedeltaIndex with a specified frequency
# Can use this TimedeltaIndex as index for a Series or DataFrame
# https://pandas.pydata.org/docs/reference/api/pandas.timedelta_range.html

td_range = pd.timedelta_range(start = '1 days', end = '10 days', freq = '2D') # '2D' means every 2 days
print(td_range)
# TimedeltaIndex(['1 days', '3 days', '5 days', '7 days', '9 days'], dtype='timedelta64[ns]', freq='2D')

td_range = pd.timedelta_range(start = '1 day', end = '2 days', freq = '6h') # '6h' means every 6 hours
print(td_range)
# TimedeltaIndex(['1 days 00:00:00', '1 days 06:00:00', '1 days 12:00:00',
#                 '1 days 18:00:00', '2 days 00:00:00'],
#                dtype='timedelta64[ns]', freq='6h')

np.random.seed(0)
s_timedelta_range = pd.Series(data = np.random.randint(0, 100, size = len(td_range)), index = td_range)
print(s_timedelta_range)
# 1 days 00:00:00    44
# 1 days 06:00:00    47
# 1 days 12:00:00    64
# 1 days 18:00:00    67
# 2 days 00:00:00    67
# Freq: 6h, dtype: int64


'''
#--------------------------
## Period data
#--------------------------
'''

#################
## pd.Period() ##
#################
# Represents a period of time.

period = pd.Period('2012-1-1', freq='D')

print(period) 
# 2012-01-01

print(type(period))
# <class 'pandas._libs.tslibs.period.Period'>

print(period.freq)
# <Day>

print(period.day)
# 1

#########################
## .Series.to_period() ##
#########################
# Convert Series from DatetimeIndex to PeriodIndex.

idx = pd.DatetimeIndex(['2023', '2024', '2025'])
s = pd.Series([1, 2, 3], index=idx)
s = s.to_period()

print(s)
# 2023    1
# 2024    2
# 2025    3
# Freq: Y-DEC, dtype: int64

print(s.index)
# PeriodIndex(['2023', '2024', '2025'], dtype='period[Y-DEC]')

#######################
## pd.period_range() ##
#######################
# Return a fixed frequency PeriodIndex (Can use this as Series or DataFrame index).
# The day (calendar) is the default frequency.

period_index = pd.period_range(start = '2017-01-01', end = '2018-01-01', freq = 'Q')
print(period_index)
# PeriodIndex(['2017Q1', '2017Q2', '2017Q3', '2017Q4', '2018Q1'], dtype='period[Q-DEC]')

np.random.seed(0)
s_period_range = pd.Series(data = np.random.randint(0, 100, size = len(period_index)), index = period_index)
print(s_period_range)
# 2017Q1    44
# 2017Q2    47
# 2017Q3    64
# 2017Q4    67
# 2018Q1    67
# Freq: Q-DEC, dtype: int64


'''
#--------------------------
## Infer the most likely frequency given the input index.
#--------------------------
'''

#####################
## pd.infer_freq() ##
#####################

idx = pd.date_range(start = '2020/12/01', end = '2020/12/30', periods = 30)

infered_freq = pd.infer_freq(idx)
print(infered_freq) # D (daily frequency)