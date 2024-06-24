import pandas as pd
import numpy as np

date_range = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
data = np.random.randn(len(date_range))

# Create a time series DataFrame
time_series_df = pd.DataFrame(data, index=date_range, columns=['Value'])

# Display the first few rows of the DataFrame
print(time_series_df.head())
