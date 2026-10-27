import numpy as np
import pandas as pd
from dfit import Dfit

# gaussian peak with constant background
def gaussian(x, A, x0, w, B):
    return A*np.exp(-(x-x0)**2/(2*w**2)) + B

# lorentzian peak with constant background
def lorentzian(x, A, x0, w, B):
    return A/(1 + ((x-x0)/w)**2) + B

# fit both functions to both data files
for filename in ['gl1.xlsx', 'gl2.xlsx']:
    print('\nData file:', filename)
    
    data = pd.read_excel('week 6/' + filename)
    
    xs = data['x'].to_numpy()
    ys = data['y'].to_numpy()

    # estimate constant background
    B_estim = np.min(ys)

    # estimate peak height above background
    A_estim = np.max(ys) - B_estim

    # estimate peak center from largest y value
    x0_estim = xs[np.argmax(ys)]

    # estimate the width from the x range
    w_estim = (np.max(xs) - np.min(xs))/10

    # estimes in the order A, x0, w, B
    estimes = [A_estim, x0_estim, w_estim, B_estim]

    # gaussian fit
    print('\nGaussian fit')
    gaussian_fit = Dfit(gaussian, xs, ys, p0s=estimes)
    gaussian_fit.printfit()
    gaussian_fit.plotfit(xlabel='x', ylabel='y',
                         title=filename + ' Gaussian')

    # lorentzian fit
    print('\nLorentzian fit')
    lorentzian_fit = Dfit(lorentzian, xs, ys, p0s=estimes)
    lorentzian_fit.printfit()
    lorentzian_fit.plotfit(xlabel='x', ylabel='y', title=filename + ' Lorentzian')
    
# for gl1.xlsx, the lorentzian model reduced chisquared = 0.00204
# compared with 0.00530 for the gaussian. 
# the lorentzian provides a better fit.

# for gl2.xlsx, the gaussian reduced chisquared = 0.00212
# compared with 0.00461 for the lorentzian.
# means the gaussian is the better model. 

# this works with the different tail behaviors 
# of the two functions.