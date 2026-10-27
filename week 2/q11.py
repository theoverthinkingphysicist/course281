import numpy as np
from numpy import sqrt, arctan2, pi

def polar(x, y):

    r = sqrt(x**2 + y**2)

    theta = arctan2(y, x)

    return r, theta

x = float(input("x? "))
y = float(input("y? "))

r, theta = polar(x, y)

print("r = %f theta = %f" % (r, theta))