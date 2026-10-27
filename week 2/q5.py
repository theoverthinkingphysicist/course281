## Calculating list statistics. Next, add on to your program
## for item 4 so it reports the total number of readings, the average of all
## the readings, and the smallest and largest reading. For this purpose
## you will want to use the len(), sum(), min(), and max() functions:

readings = []

while True:
    reading = float(input("Enter reading (<0 to stop): "))
    
    if reading < 0:
        break
    
    readings.append(reading)
    
print("Readings: ", readings)

count = len(readings)
print("Number of readings: ", count)

if count > 0:
    average = sum(readings) / count
    print("Average reading: ", average)

    print("Smallest reading: ", min(readings))
    print("Largest reading: ", max(readings))
else:
    print("No readings entered! :(")