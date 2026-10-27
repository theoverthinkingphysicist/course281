import numpy as np
import matplotlib.pyplot as plt

# x values
x = np.linspace(-2*np.pi, 2*np.pi, 400)

plt.figure(figsize=(10, 12))

# y = x
plt.subplot(3, 2, 1)
plt.plot(x, x, color="red")
plt.title("y = x")
plt.xlabel("x")
plt.ylabel("y")

# y = x^2
plt.subplot(3, 2, 2)
plt.plot(x, x**2, color="orange")
plt.title("y = x²")
plt.xlabel("x")
plt.ylabel("y")

# y = sin(x)
plt.subplot(3, 2, 3)
plt.plot(x, np.sin(x), color="yellow")
plt.title("y = sin(x)")
plt.xlabel("x")
plt.ylabel("y")

# y = cos(x)
plt.subplot(3, 2, 4)
plt.plot(x, np.cos(x), color="green")
plt.title("y = cos(x)")
plt.xlabel("x")
plt.ylabel("y")

# y = exp(x)
plt.subplot(3, 2, 5)
plt.plot(x, np.exp(x), color="blue")
plt.title("y = exp(x)")
plt.xlabel("x")
plt.ylabel("y")

# y = tan(x)
plt.subplot(3, 2, 6)
plt.plot(x, np.tan(x), color="purple")
plt.title("y = tan(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.ylim(-10, 10)

# ok
plt.subplots_adjust(hspace=0.5)
plt.show()