import pandas as pd

start_date = '2024-01-01'
end_date = '2024-01-05'
date_index = pd.date_range(start=start_date, end=end_date, freq='D')

#setting TimeZone
date_index = pd.date_range(start=start_date, end=end_date, freq='D', tz='UTC')
print(date_index)

#Localizing TimeZone
date_index = pd.date_range(start=start_date, end=end_date, freq='D')
date_index = date_index.tz_localize('America/New_York')
print(date_index)

#Converting TimeZone
date_index = date_index.tz_convert('Europe/London')
print(date_index)

#Combining two different TimeZones
date_index1 = pd.date_range(start=start_date, periods=3, freq='D', tz='UTC')
date_index2 = pd.date_range(start=start_date, periods=3, freq='D', tz='America/New_York')
combined_index = date_index1.union(date_index2)
print(combined_index)
