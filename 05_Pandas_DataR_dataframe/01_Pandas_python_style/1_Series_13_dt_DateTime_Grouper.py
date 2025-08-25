'''
The pandas.Series.dt accessor is a powerful interface 
that provides access to datetime-like properties and methods for pandas Series.

Supported Types: datetime64[ns], datetime64[ns, tz], Period, timedelta[ns]

Flow of contents:
0. Creating a Series with datetime data:
    + Datetime data: pd.to_datetime(), astype('datetime64[ns]'), pd.date_range(), pd.bdate_range()
    + Timedelta data: pd.to_timedelta(), astype('timedelta64[ns]'), pd.timedelta_range()
    + Period: pd.period(), .Series.to_period(), pd.period_range(), 
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


