# writing to a text file

import numpy as np
import pandas as pd

rr = int(input("rows? "))
cc = int(input("cols? "))

aa = np.zeros((rr,cc), int)

for r in range(rr):
    for c in range(cc):
        aa[r,c] = r * cc + c + 1
    
np.savetxt("foo.txt", aa, fmt="%.3f")
