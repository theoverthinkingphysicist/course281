import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# 20 < x < 20, −20 < y < 20

def psi(x, y):
    r = np.sqrt(x**2 + y**2)
    return x * (6 - r) * np.exp(-r/3)

x = np.linspace(-20, 20, 200)
y = np.linspace(-20, 20, 200)
X, Y = np.meshgrid(x, y)
Z = psi(X, Y)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='twilight', edgecolor='none')

ax.set_title(r'Hydrogen Orbital: $n=3,\ \ell=1,\ m=0$')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel(r'$\psi(x,y)$')
fig.colorbar(surf, ax=ax, shrink=0.6)
plt.show()