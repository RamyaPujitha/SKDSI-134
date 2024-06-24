import pandas as pd
import matplotlib.pyplot as plt

sales_data = {
    'Product A': [4, 7, 1, 8, 5],
    'Product B': [5, 2, 8, 3, 6],
    'Product C': [7, 5, 3, 4, 9]
}

categories = ['Store 1', 'Store 2', 'Store 3', 'Store 4', 'Store 5']

sales_df = pd.DataFrame(sales_data, index=categories)

ax1 = sales_df.plot(kind='bar', figsize=(10, 6))
ax1.set_xlabel('Stores')
ax1.set_ylabel('Sales')
ax1.set_title('Side-by-Side Bar Plot of Sales')
plt.xticks(rotation=0)
plt.show()

ax2 = sales_df.plot(kind='bar', stacked=True, figsize=(10, 6))
ax2.set_xlabel('Stores')
ax2.set_ylabel('Sales')
ax2.set_title('Stacked Bar Plot of Sales')
plt.xticks(rotation=0)
plt.show()
