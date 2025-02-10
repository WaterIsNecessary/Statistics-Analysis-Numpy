import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

print("This programme calculates the binomial distribution for an event A given it's probability of occurring is P and the number of attempts is N.")
userNCount = int(input("Please input the number of trials: "))
userProb = float(input("Please input the probability of Event A occurring for each trial: "))
numOccurrences = np.arange(userNCount + 1)
pmfBinDist = binom.pmf(numOccurrences, userNCount, userProb)
cdfBinDist = binom.cdf(numOccurrences, userNCount, userProb)

# 15 inches wide and 7.5 tall figure container for subplots
plt.figure(figsize=(15, 7.5))

# Create a grid with 1 row and 2 columns. Place this chart in the first row first column 
plt.subplot(1, 2, 1)
# Create histogram with numOccurrences on x-axis and PMF on y-axis, blue transparency 50%
plt.bar(numOccurrences, pmfBinDist, color='blue', alpha=0.5)
# Labels
plt.xlabel('Number of occurrences of A (A being success)', fontweight='bold')
plt.ylabel('Probability of Success', fontweight='bold')
plt.title('Probability Mass Function', fontweight='bold')

# Create a grid with 1 row and 2 columns. Place this chart in the first row second column
plt.subplot(1, 2, 2)
# Create histogram with numOccurrences on x-axis and CDF on y-axis, red transparency 50%
plt.bar(numOccurrences, cdfBinDist, color='red', alpha=0.5)
# Labels
plt.xlabel('Number of occurrences of A (A being success)', fontweight='bold')
plt.ylabel('Cumulative Probability of Success' , fontweight='bold')
plt.title('Cumulative Distribution Function', fontweight='bold')

# Adjusts both plots to fit properly within the figure
plt.tight_layout()
# Displays Figure containing subplots
plt.show()