import numpy as np
import matplotlib.pyplot as plt

r = 5
N = 20

xlist = []
ylist = []
zlist = []

for theta in np.linspace(0, np.pi, N):
    for phi in np.linspace(0, 2*np.pi, N):

        x = r * np.sin(theta) * np.cos(phi)
        y = r * np.sin(theta) * np.sin(phi)
        z = r * np.cos(theta)

        xlist.append(x)
        ylist.append(y)
        zlist.append(z)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(xlist, ylist, zlist, c=zlist, cmap='coolwarm', s=15)

ax.set_title('3D Scatter Plot of Points on a Sphere')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()