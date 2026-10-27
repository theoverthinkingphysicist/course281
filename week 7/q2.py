import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_excel("week 7/decay1.xlsx")   # long data set (0 to 200 min)
data2 = pd.read_excel("week 7/decay2.xlsx")   # short data set (0 to 50 min)

t1 = data1.iloc[:, 0].to_numpy(dtype=float)
N1 = data1.iloc[:, 1].to_numpy(dtype=float)
t2 = data2.iloc[:, 0].to_numpy(dtype=float)
N2 = data2.iloc[:, 1].to_numpy(dtype=float)

# uncertainity for each point
sigma1 = np.sqrt(N1)
sigma2 = np.sqrt(N2)

def make_plot(t, N, sigma, title, log_axis):
    plt.figure()
    plt.errorbar(t, N, yerr=sigma, fmt="o", markersize=3)
    plt.xlabel("t (min)")
    plt.ylabel("N (counts/min)")
    plt.title(title)
    if log_axis:
        plt.yscale("log")

# parts (a) and (b): linear axes with error bars
make_plot(t1, N1, sigma1, "decay1, linear", log_axis=False)
make_plot(t2, N2, sigma2, "decay2, linear", log_axis=False)

# part (c): same plots with a logarithmic y-axis
make_plot(t1, N1, sigma1, "decay1, log y-axis", log_axis=True)
make_plot(t2, N2, sigma2, "decay2, log y-axis", log_axis=True)

plt.show()