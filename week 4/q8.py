# labeling plots

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 10

x = np.linspace(-2*np.pi, 2*np.pi, 20)

f1 = np.sin(x)
f2 = np.cos(x)

plt.figure(figsize=(8, 5))

plt.plot(x, f1, 's-', color='magenta', label='sin(x)')
plt.plot(x, f2, '*--', color='purple', label='cos(x)')

plt.title('sin(x) and cos(x) --> plot from q7', fontsize=12)
plt.xlabel('x values', fontsize=11)
plt.ylabel('function value', fontsize=11)

plt.legend(fontsize=12)

plt.grid(True)
plt.ylim(-2, 2)

plt.show()