import numpy as np
import pandas as pd
from dfit import Dfit

data = pd.read_excel('week 6/peak4.xlsx')
xs = data['x (cm)'].to_numpy()
ys = data['y (mV)'].to_numpy()

def gaussian_linear(x, A, x0, w, B, m):
    return A*np.exp(-(x-x0)**2/(2*w**2)) + B + m*x

# NEW gaussian with quadratic background
def gaussian_quadratic(x, A, x0, w, B, m, c):
    return (A*np.exp(-(x-x0)**2/(2*w**2))
            + B + m*x + c*x**2)

# fit og model with 5 parameters
print('\nLinear background')

linear_fit = Dfit(gaussian_linear, xs, ys, p0s=[3, 4, 1, 2, 0])
linear_fit.printfit()
linear_fit.plotfit(xlabel='x (cm)', ylabel='y (mV)')

# fit new model with 6 parameters
print('\nQuadratic background')

# start the new quadratic coefficient at zero
quadratic_fit = Dfit(gaussian_quadratic, xs, ys, p0s=[3, 4, 1, 2, 0, 0])
quadratic_fit.printfit()
quadratic_fit.plotfit(xlabel='x (cm)', ylabel='y (mV)')

# the reduced chisquared decreased from approx 0.0176 
# to 0.0100. quad coeff is statistically distingushiable from 0
# adding the quad term is justified as it improves the fit
# and represents a contrib to the earlier model