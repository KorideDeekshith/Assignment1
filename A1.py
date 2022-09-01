#Importing libraries to find median and mean 
from statistics import median as m
from statistics import mean
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# To sort the age
ages.sort()
print(ages)

#To find the max and min age
max = max(ages)
min = min(ages)
print(min)
print(max)

#To add the max and min age to the list
ages.append(min)
ages.append(max)
print(ages)

#To find the median, mean and range
print(m(ages))
print(mean(ages))
range= max-min
print(range)