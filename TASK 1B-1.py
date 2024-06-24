import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(0, 10, 100)
sine_values = np.sin(x_values)
cosine_values = np.cos(x_values)

fig, (ax_sine, ax_cosine) = plt.subplots(2, 1, figsize=(10, 8))

ax_sine.plot(x_values, sine_values, label='sin(x)', color='blue', linestyle='-')
ax_sine.set_title('Sine Function')
ax_sine.set_xlabel('x-axis')
ax_sine.set_ylabel('sin(x)')
ax_sine.grid(True)
ax_sine.legend(loc='upper right')
ax_sine.set_xticks(np.arange(0, 11, 1))
ax_sine.set_yticks(np.arange(-1, 1.5, 0.5))
ax_sine.set_xticklabels([f'{i}' for i in range(11)])
ax_sine.set_yticklabels([f'{i:.1f}' for i in np.arange(-1, 1.5, 0.5)])
ax_sine.annotate('Max Value', xy=(np.pi/2, 1), xytext=(np.pi/2+1, 0.8),arrowprops=dict(facecolor='black', shrink=0.05))

ax_cosine.plot(x_values, cosine_values, label='cos(x)', color='red', linestyle='--')
ax_cosine.set_title('Cosine Function')
ax_cosine.set_xlabel('x-axis')
ax_cosine.set_ylabel('cos(x)')
ax_cosine.grid(True)
ax_cosine.legend(loc='upper right')
ax_cosine.set_xticks(np.arange(0, 11, 1))
ax_cosine.set_yticks(np.arange(-1, 1.5, 0.5))
ax_cosine.set_xticklabels([f'{i}' for i in range(11)])
ax_cosine.set_yticklabels([f'{i:.1f}' for i in np.arange(-1, 1.5, 0.5)])
ax_cosine.annotate('Min Value', xy=(np.pi, -1), xytext=(np.pi+1, -0.8),arrowprops=dict(facecolor='black', shrink=0.05))

plt.tight_layout()
plt.savefig('line_plot_with_annotations.png')
plt.show()
