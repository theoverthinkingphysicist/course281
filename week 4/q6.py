# plotting

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 200)

print("x values:")
print(x)

f1 = np.sin(x)
f2 = np.cos(x)

print("\nf1 = sin(x):")
print(f1)

print("\nf2 = cos(x):")
print(f2)

# sinx
plt.figure()
plt.plot(x, f1, 'b-', label='sin(x)')
plt.title('f1(x) = sin(x)')
plt.xlabel('x')
plt.ylabel('f1(x)')
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.legend()
plt.show()

# cosx
plt.figure()
plt.plot(x, f2, 'r-', label='cos(x)')
plt.title('f2(x) = cos(x)')
plt.xlabel('x')
plt.ylabel('f2(x)')
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.legend()
plt.show()

# together <3
plt.figure()
plt.plot(x, f1, 'b-', label='sin(x)')
plt.plot(x, f2, 'r-', label='cos(x)')
plt.title('sin(x) and cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

# force limits
plt.ylim(-2, 2)

plt.show()