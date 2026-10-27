import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self,x=0.0,y=0.0):
        self.x = x
        self.y = y
        
# a.
particles = []

for x in np.linspace(-5, 5, 50):
    for y in np.linspace(-5, 5, 50):

        r = np.sqrt(x**2 + y**2)

        if r > 3 and r < 5:
            particles.append(Particle(x, y))

for p in particles:
    plt.plot(p.x, p.y, 'ro', markersize=2)

plt.title('Particles in a Ring')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.show()

# b. 
N = 50
R = 10

particles = []

for theta in np.linspace(0, 2*np.pi, N, endpoint=False):

    x = R * np.cos(theta)
    y = R * np.sin(theta)

    particles.append(Particle(x, y))
    
for p in particles:
    plt.plot(p.x, p.y, 'bo')

plt.title('50 Particles on a Circle of Radius 10')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.show()