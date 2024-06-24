import pandas as pd

# Using Start date and End date
start_date = '2024-01-01'
end_date = '2024-12-31'
datetime_index = pd.date_range(start=start_date, end=end_date)
print(datetime_index)

# Using Start date and Periods
import pandas as pd
start_date = '2024-01-01'
number_of_days = 365  # for a full year
datetime_index = pd.date_range(start=start_date, periods=number_of_days)
print(datetime_index)

# Using End date and Periods
import pandas as pd
end_date = '2024-12-31'
number_of_days = 365  # for a full year
datetime_index = pd.date_range(end=end_date, periods=number_of_days)
print(datetime_index)

# Using Frequency
import pandas as pd
start_date = '2024-01-01'
end_date = '2024-12-31'
datetime_index = pd.date_range(start=start_date, end=end_date, freq='D') # 'D' generates dates on a daily basis
print(datetime_index)
