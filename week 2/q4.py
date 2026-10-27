## Building lists. Let’s imagine you are running an experiment
## and you have taken a bunch of readings (of voltages, for example) that
## are floating-point numbers, always positive. Write a program that asks
##you for the readings one at a time and builds up a list of the data.
## After you have entered the last reading, you enter a negative value to
## signify that there are no more readings, and then the program prints
## out the whole list:

readings = []

while True:
    reading = float(input("Enter reading (<0 to stop): "))
    
    if reading < 0:
        break
    
    readings.append(reading)
    
print("Readings: ", readings)
    
## if print function stays within the while block, it prints out 
## the status of the ongoing list for every number
## i.e you enter 2, it prints out Readings:  [2.0] and ongoing...