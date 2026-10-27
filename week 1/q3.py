# 3. Calculate a physics equation.

from numpy import sqrt
G = 9.8 # accel of gravity, m/s**
z = float(input("Enter z (m): "))
t = sqrt(2*z/G)
print("t =", t, "s")