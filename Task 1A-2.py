import pandas as pd


sales_data = [100, 200, 300, 400, 500, 600]
multi_index = pd.MultiIndex.from_tuples([('North', 2021), ('North', 2022), ('South', 2021), ('South', 2022), ('East', 2021), ('East', 2022)])
sales_series = pd.Series(sales_data, index=multi_index)

print("Sales Series with MultiIndex:")
print(sales_series)


subset_north = sales_series.loc['North']
print("\nSubset North:")
print(subset_north)

subset_north_2022 = sales_series.loc[('North', 2022)]
print("\nSubset North, Year 2022:")
print(subset_north_2022)

subset_south = sales_series.loc['South']
print("\nSubset South:")
print(subset_south)

subset_east_2021 = sales_series.loc[('East', 2021)]
print("\nSubset East, Year 2021:")
print(subset_east_2021)

subset_south_xs = sales_series.xs('South')
print("\nSubset South using xs:")
print(subset_south_xs)

subset_year_2022 = sales_series.xs(2022, level=1)
print("\nSubset Year 2022 using xs:")
print(subset_year_2022)
