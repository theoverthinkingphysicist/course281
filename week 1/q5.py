# 5. Using functions from scipy.special.

from numpy import sqrt
from scipy.special import ellipe

a = float(input("Enter a: "))
b = float(input("Enter b: "))

e = sqrt(1-b**2/a**2)

C = 4*a*ellipe(e)

print("C =", C)