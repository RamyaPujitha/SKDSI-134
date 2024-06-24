import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

observations = np.random.normal(loc=0, scale=1, size=1000)

plt.figure(figsize=(10, 6))
plt.hist(observations, bins=30, edgecolor='black', alpha=0.7)
plt.xlabel('Observed Value')
plt.ylabel('Frequency')
plt.title('Histogram of Observed Value Frequency')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
sns.kdeplot(observations, fill=True)
plt.xlabel('Observed Value')
plt.ylabel('Density')
plt.title('Density Plot of Continuous Probability Distribution')
plt.grid(True)
plt.show()
