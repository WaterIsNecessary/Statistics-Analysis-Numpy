import numpy as np

heightsArray = np.loadtxt('data.txt', delimiter=',')

median = np.median(heightsArray)

mean = np.mean(heightsArray)

## Added ddof=1 to emulate sample variance, where the denominator is n-1 not n
variance = np.var(heightsArray, ddof=1)

## Added ddof=1 to emulate sample standard deviation, where the denominator is n-1 not n
standardDeviation = np.std(heightsArray, ddof=1)

print(f"The median is: {median}")
print(f"The mean is: {mean}")
print(f"The sample variance is: {variance}")
print(f"The sample standard deviation is: {standardDeviation}")

