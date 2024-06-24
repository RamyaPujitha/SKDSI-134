import pandas as pd
import numpy as np

# Creating a dictionary with renamed variables
data = {
    'ID': [1, 2, np.nan, 4, 5, np.nan, 7],
    'Value': [np.nan, 2, 3, 4, np.nan, 6, 7],
    'Category': ['foo', 'bar', 'baz', np.nan, 'qux', 'quux', 'corge'],
    'Score': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
}

# Creating DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Identifying missing data
missing_data = df.isna()
print("\nMissing Data in DataFrame:")
print(missing_data)

# Dropping rows with any missing data
df_dropna_rows = df.dropna()
print("\nDataFrame after dropping rows with any missing data:")
print(df_dropna_rows)

# Dropping columns with any missing data
df_dropna_cols = df.dropna(axis=1)
print("\nDataFrame after dropping columns with any missing data:")
print(df_dropna_cols)

# Filling missing data using fillna function
df_fillna = df.fillna(value={'ID': df['ID'].mean(), 'Value': df['Value'].mean(), 'Category': 'missing', 'Score': 0})
print("\nDataFrame after filling missing data:")
print(df_fillna)

# Adding a duplicate row for demonstration
df_with_duplicates = df.append(df.iloc[2], ignore_index=True)
print("\nDataFrame with Duplicates:")
print(df_with_duplicates)

# Identifying duplicates
duplicates = df_with_duplicates.duplicated()
print("\nDuplicates in DataFrame:")
print(duplicates)

# Removing duplicates
df_no_duplicates = df_with_duplicates.drop_duplicates()
print("\nDataFrame after removing duplicates:")
print(df_no_duplicates)
