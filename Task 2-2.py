import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
x = np.random.rand(100)
y = 2 * x + np.random.normal(0, 0.1, 100)


plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.7)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot of X vs. Y')
plt.grid(True)
plt.show()
