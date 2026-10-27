import numpy as np
import matplotlib.pyplot as plt

def psi(x, y):
    r = np.sqrt(x**2 + y**2)
    return x * (6 - r) * np.exp(-r/3)

x = np.linspace(-20, 20, 500)
y = np.linspace(-20, 20, 500)
X, Y = np.meshgrid(x, y)
Z = psi(X, Y)

plt.figure(figsize=(8, 6))
plt.imshow(Z, extent=[-20, 20, -20, 20], origin='lower', cmap='twilight')
plt.colorbar(label=r'$\psi(x,y)$')
plt.title(r'Density Plot of $\psi(x,y)=x(6-r)e^{-r/3}$')
plt.xlabel('x')
plt.ylabel('y')
plt.show()