import numpy as np
import pandas as pd
from dfit import Dfit

# peak data (EBK)
data = pd.read_excel('week 6/peak4.xlsx')

xs = data['x (cm)'].to_numpy()
ys = data['y (mV)'].to_numpy()

# def gaussian peak + linear bcgr
def gaussian_linear(x, A, x0, w, B, m):
    return A*np.exp(-(x-x0)**2/(2*w**2)) + B + m*x

# og estimates from q4.py
guesses = [3, 4, 1, 2, 0]

print('\nOriginal guesses')

# fit data using og guesses
myfit = Dfit(gaussian_linear, xs, ys, p0s=guesses)

# results
myfit.printfit()

# plot andmodel
myfit.plotfit(xlabel='x (cm)', ylabel='y (mV)')

# now...lets change every estim to 1 just for fun
guesses = [1, 1, 1, 1, 1]

print('\nAll guesses = 1')

# repeatfit
myfit = Dfit(gaussian_linear, xs, ys, p0s=guesses)
myfit.printfit()
myfit.plotfit(xlabel='x (cm)', ylabel='y (mV)')

# this is me experimenting with other initial estim
guess_sets = [[3, 5, 0.5, 2, 0], [3, 5, 1, 1, 0], [2, 5, 1, 2, 0]]

for guesses in guess_sets:
    
    print('\nInitial guesses:', guesses)

    # try the fit and check whether it converges
    try:
        myfit = Dfit(gaussian_linear, xs, ys, p0s=guesses)
        myfit.printfit()
        myfit.plotfit(xlabel='x (cm)', ylabel='y (mV)')

    except RuntimeError:
        print('does not converge :/ scrap')
        
# using the original guesses [3, 4, 1, 2, 0]
# the fit converged to a reduced chisquared of 
# approx 0.0176. BUT when all parameters were 
# initially set to 1, the reduced chisquared inc
# to approx 0.392, meaningit was a worse fit. 
# opther guesses closer to the gaussian peak still 
# converged to the original result. 
# thus we can conclude that nonlinear leastsquares 
# fitting is sensitive to initial guesses and can 
# converge to local minima