## 0 pts - Practice with range(). Use for, range(), append() to
## built up and print out the following lists:
## • The integers 0 to 10
## • The integers 1 to 10
## • The integers 3 to 27 in steps of 3
## • The integers 50 to 10 in descending steps of 10

## range(start, stop, step) EXCLUDES the stop value
## if step is omitted it defaults to 1

list_1 = []
for number in range(0, 11):
    list_1.append(number)
print(list_1)

list_2 = []
for number in range(1, 11):
    list_2.append(number)
print(list_2)

list_3 = []
for number in range(3, 28, 3):
    list_3.append(number)
print(list_3)

list_4 = []
for number in range(50, 0, -10):
    list_4.append(number)
print(list_4)
