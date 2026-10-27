## Repeating a calculation until user is done. Next, modify
## your program for item 2 so it asks you for s and does the calculation,
## and repeats this until you enter a negative s

while True:
    s = float(input("Enter s <0 to stop: "))
    
    if s < 0:
        break
    
    N = 0
    total = 0

    while total <= s:
        N = N + 1
        total = total + N**3
    
    print(f"Smallest sum of n**3 greater than {s:g} is {total}") 

## g kills the decimal point i.e 100.0 = 100