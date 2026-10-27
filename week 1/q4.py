# 4. Another physics equation.

from numpy import sqrt, cos, pi, deg2rad
G = 9.8 # accel of gravity, m/s**
L = float(input("Enter L (m): "))
beta_deg = float(input("Enter beta (degrees): "))

## beta_rad = beta_deg*pi/180

T = 2*pi*sqrt(L*cos(deg2rad(beta_deg))/G)
print("T =", T, "s")