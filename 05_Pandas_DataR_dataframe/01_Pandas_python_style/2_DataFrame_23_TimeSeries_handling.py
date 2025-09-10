import pandas as pd

##################################
## Read the Air Quality dataset ##
##################################

df_aq = (
    pd.read_csv("05_Pandas_DataR_dataframe/data/air_quality_no2_long.csv")
    .rename(columns={"date.utc": "date"})
)

print(df_aq.head())
#     city country                       date location parameter  value   unit
# 0  Paris      FR  2019-06-21 00:00:00+00:00  FR04014       no2   20.0  µg/m³
# 1  Paris      FR  2019-06-20 23:00:00+00:00  FR04014       no2   21.8  µg/m³
# 2  Paris      FR  2019-06-20 22:00:00+00:00  FR04014       no2   26.5  µg/m³
# 3  Paris      FR  2019-06-20 21:00:00+00:00  FR04014       no2   24.9  µg/m³
# 4  Paris      FR  2019-06-20 20:00:00+00:00  FR04014       no2   21.4  µg/m³

