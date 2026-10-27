## Using list comprehensions. Create the following lists using
## list comprehensions, and print them out:
## • The integers 0 to 20
## • The integers 0 to 20, omitting integers divisible by 5
## • The integers 0 to 20, including only integers divisible by 5
## • A list of of all integers a + b formed by taking a from the list
## [10,20,30] and b from the list [3,7,9]. Your output should
## start [13,17,19,23,27,....

list_1 = [number for number in range(21)]
print(list_1)

list_2 = [number for number in range(21) if number % 5 != 0]
print(list_2)

list_3 = [number for number in range(21) if number % 5 == 0]
print(list_3)

list_4 = [a + b for a in [10, 20, 30] for b in [3, 7, 9]]
print(list_4)