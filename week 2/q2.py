## Using the while statement. Write a program that finds
## the smallest N for which (PN
## 1 n3) > s for any given s, then prints out
## s and the sum. For the first version of your program, s should be a
## constant in your program (that is, it should be set by an assignment
## statement). For example, if you set s = 1000 your program should
## print

s = 1000
N = 0
total = 0

while total <= s:
    N = N + 1
    total = total + N**3
    
print(f"Smallest sum of n**3 greater than {s} is {total}")