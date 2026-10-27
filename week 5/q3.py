# a.
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 500)
y = np.linspace(-10, 10, 500)
X, Y = np.meshgrid(x, y)

R = np.sqrt(X**2 + Y**2)
Theta = np.arctan2(Y, X)
S = np.cos(R + Theta)

plt.figure(figsize=(6,6))
plt.imshow(S, extent=[-10,10,-10,10], origin='lower', cmap='RdYlBu_r')
plt.colorbar(label='s(x,y)')
plt.title(r'$s(x,y)=\cos(r+\theta)$')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# b.
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 500)
y = np.linspace(-10, 10, 500)
X, Y = np.meshgrid(x, y)

R = np.sqrt(X**2 + Y**2)
Theta = np.arctan2(Y, X)
W = np.cos(R + Theta/2)

plt.figure(figsize=(6,6))
plt.imshow(W, extent=[-10,10,-10,10], origin='lower', cmap='viridis')
plt.colorbar(label='w(x,y)')
plt.title(r'$w(x,y)=\cos(r+\theta/2)$')
plt.xlabel('x')
plt.ylabel('y')
plt.show()