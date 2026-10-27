# array slicing

import numpy as np

rr = int(input("rows? "))
cc = int(input("cols? "))

aa = np.zeros((rr,cc), int)

for r in range(rr):
    for c in range(cc):
        aa[r,c] = r * cc + c + 1
        
print('array:\n', aa)  

print("fourth column: ", aa[:,3])
print("fourth row: ", aa[3,:])

print("upper left:\n", aa[:3, :3])
print("upper right:\n", aa[:3, -3:])

print("transpose:\n", aa.T)