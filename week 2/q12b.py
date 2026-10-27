import numpy as np
from numpy import sqrt, arctan2

def polar(x, y):

    # calc radial distance from the origin
    r = sqrt(x**2 + y**2)

    # arctan2(y, x) automatically determines the correct quadrant
    # and returns an angle between -pi and pi
    theta = arctan2(y, x)

    return float(r), float(theta)


# test points
print("Quadrant I:  ", polar(1, 1))
print("Quadrant II: ", polar(-1, 1))
print("Quadrant III:", polar(-1, -1))
print("Quadrant IV: ", polar(1, -1))