import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(0)

sales_data = {
    'Region': np.random.choice(['North', 'South', 'East', 'West', 'Central'], 100),
    'Sales': np.random.randn(100)
}

sales_df = pd.DataFrame(sales_data)


plt.figure(figsize=(12, 6))
sns.boxplot(x='Region', y='Sales', data=sales_df)
plt.xlabel('Region')
plt.ylabel('Sales')
plt.title('Box Plot of Sales by Region')
plt.grid(True)
plt.show()
