# more plots

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 20)

f1 = np.sin(x)
f2 = np.cos(x)

plt.figure(figsize=(8,5))

plt.plot(x, f1, 's-', color='magenta', label='sin(x)')
plt.plot(x, f2, '*--', color='purple', label='cos(x)')

plt.title('sin(x) and cos(x) --> ref from q6')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-2, 2)

plt.grid(True)
plt.show()