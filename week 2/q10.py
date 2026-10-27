## instructions too big to fit on here :(
    
n_max = int(input("n_max? "))

for n in range(1, n_max + 1): ## smallification./...
   count = 0
   
   for l in range(n):
       for m in range (-l, l + 1):
           
           print(f"n = {n}  n = {l}  n = {m}")
           
           count = count + 1
           
   print(f"Total states with n = {n} : {count}") 