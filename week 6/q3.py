import numpy as np
import pandas as pd
from dfit import Dfit

# read the file containing x and y, but NO yerr
data = pd.read_excel('week 6/data3.xlsx')

# convert the columns to numpp arrays
xs = data['x (cm)'].to_numpy()
ys = data['y (micro-m)'].to_numpy()

# define polynomials of increasing order
def poly1(x, a0, a1):
    return a0 + a1*x
def poly2(x, a0, a1, a2):
    return a0 + a1*x + a2*x**2
def poly3(x, a0, a1, a2, a3):
    return a0 + a1*x + a2*x**2 + a3*x**3
def poly4(x, a0, a1, a2, a3, a4):
    return a0 + a1*x + a2*x**2 + a3*x**3 + a4*x**4
def poly5(x, a0, a1, a2, a3, a4, a5):
    return (a0 + a1*x + a2*x**2 + a3*x**3 + a4*x**4 + a5*x**5)

# put functions into a list
fits = [poly1, poly2, poly3, poly4, poly5]

# fit each polynomial to the data
for order, model in enumerate(fits, start=1):

    print(f'\nPolynomial order {order}')

    # mno yerrs are supplied for this data :(
    myfit = Dfit(model, xs, ys, datname='data3')

    # print the fitting results
    myfit.printfit()

    # plot the data and the fit
    myfit.plotfit(xlabel='x (cm)', ylabel='y (micro-m)')
    
    # the reduced chisquared decreased
    # from approx 0.976 for the linear fit 
    # to 0.0546 for the cubic fit. 
    # higher-order polynomials did not provide much
    # improvementvand the quartic coeff was not 
    # statistically significant. so a cubic polynomial 
    # is the simplest justified model