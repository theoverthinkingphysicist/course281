# latex commands in plot labels

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 20)

f1 = np.sin(x)
f2 = np.cos(x)

plt.figure(figsize=(8,5))

plt.plot(x, f1, 's-', color='pink', label=r'$\sin(x)$')
plt.plot(x, f2, '*--', color='orange', label=r'$\cos(x)$')

plt.title(r'plot of $\sin(x)$ and $\cos(x)$ for $-\!2\pi \leq x \leq 2\pi$', fontsize=14)

plt.xlabel(r'angle $\theta$ (radians)', fontsize=12)
plt.ylabel(r'function value $f(\theta)$', fontsize=12)

plt.grid(True)
plt.legend(fontsize=10)

plt.show()