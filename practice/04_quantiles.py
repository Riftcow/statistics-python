import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import statistics
import seaborn as sns

#   create a Array of for example presentation
shirt_size = np.array([3, 4, 9, 17, 18, 20, 22, 23, 29, 32, 39, 42, 42, 42, 51, 97])

#   --Find Min Median Max
shirt_min = shirt_size.min()
shirt_max = shirt_size.max()


#   --  Debug test section...
print("shirt Minimum : ", shirt_min)
print("shirt Maximum : ", shirt_max)
print("Median for Shirt Size : ", np.median(shirt_size))

#   --  Find the Quantiles For Shirt size Array...
statistics.quantiles(shirt_size.tolist())
print("Quantiles : ", statistics.quantiles(shirt_size.tolist()))  #   debug data..

#   --  Plot data
# plt.figure(figsize=(16, 6))
sns.boxplot(shirt_size)
plt.ylabel("Shirt Label")
plt.show()
