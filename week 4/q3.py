# numpy arrays

import numpy as np

rr = int(input("rows? "))
cc = int(input("cols? "))

aa = np.zeros((rr,cc), int)

for r in range(rr):
    for c in range(cc):
        aa[r,c] = r * cc + c + 1
        
print('array:\n', aa)  