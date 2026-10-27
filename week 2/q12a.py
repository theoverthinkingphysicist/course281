import numpy as np
from numpy import sqrt, arctan, pi

def polar(x, y):

    ## radial distance from the origin
    r = sqrt(x**2 + y**2)

    ## arctan(y/x) only returns angles between -pi/2 and pi/2,
    ## so we need to correct theta depending on the quadrant.

    ## quadrants I and IV: x is positive, so arctan(y/x)
    ## already gives the correct angle
    if x > 0:
        theta = arctan(y/x)

    ## quadrant II: x is negative and y is positive
    ## add pi to move the angle into the correct quadrant
    elif x < 0 and y >= 0:
        theta = arctan(y/x) + pi

    ## quadrant III: x and y are both negative
    ## subtract pi so theta stays in the required range -pi < theta <= pi
    elif x < 0 and y < 0:
        theta = arctan(y/x) - pi

    ## if x = 0, y/x would cause division by zero
    elif x == 0 and y > 0:
        theta = pi/2

    elif x == 0 and y < 0:
        theta = -pi/2

    ## at the origin, r = 0 and there is no unique direction
    else:
        theta = 0

    return float(r), float(theta)

# test points
print("Quadrant I:  ", polar(1, 1))
print("Quadrant II: ", polar(-1, 1))
print("Quadrant III:", polar(-1, -1))
print("Quadrant IV: ", polar(1, -1))