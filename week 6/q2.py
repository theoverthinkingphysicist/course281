import numpy as np
import pandas as pd
from dfit import Dfit

# reqad data
data = pd.read_excel('week 6/data2.xlsx')

# hi look at column names
print(data.columns)

# convert these into numpy arrays
xs = data['x (cm)'].to_numpy()
ys = data['y (micro-m)'].to_numpy()
yerrs = data['yerr'].to_numpy()

# defining fifth order polynomial
def polynomial(x, p0, p1, p2, p3, p4, p5):
    return (p0 + p1*x + p2*x**2 + p3*x**3 + p4*x**4 + p5*x**5)

# compare polynomial fits of different orders
for order in range(1, 6):

    # allow only the parameters needed for this order to vary
    varies = [i <= order for i in range(6)]

    print(f'\nPolynomial order {order}')

    # fit the data ie Dfit
    myfit = Dfit(polynomial, xs, ys, yerrs, varies=varies)

    # print fitted parameters/uncertainties/chisquared
    myfit.printfit()

    # plot the data and fitted polynomial
    myfit.plotfit(xlabel='x', ylabel='y', title=f'Polynomial order {order}')
    
# red chi squared >> 1 model may not describe the data adequately
# red chi squared approx 1 model is reasonably consistent with the data
# red chi squared << 1 uncertainties may be overestimated, or the fit may be unusually close

# the linear model has a reduced chisquared of 
# approx 1.19, which is already close to one. 
# increasing the polynomial order does not improve 
# the reduced chisquared.
# the quadratic coefficient is smaller than its 
# 2sigma uncertainty.this means that it is not 
# statistically significant. thus the linear model 
# is the simplest justified fit YAY