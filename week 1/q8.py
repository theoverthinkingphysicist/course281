# 8. Find the limits of values for floats and ints.

x = float(input("enter a float: "))
print("x**2 =", x**2)

# floats can take numbers up
# to the 300th power approximately!! i tested 400 
# anything higher goes to inf, overflows
# and the smallest float cannot be 
# under the approx. -300th power (divets to 0.0)

x = int(float(input("enter an int: ")))
print("x**2 =", x**2)

import sys
print(sys.float_info)

# it seems like ints dont have a fixed largest 
# value and they can become arbituarily large cuz 
# memory storage knows no bounds! conversion did mess up output tho

# natively in binary therefore the number will be odd
# check out https://en.wikipedia.org/wiki/Double-precision_floating-point_format