#       @FU4Y
#   Library import...

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import normal, uniform
import seaborn as sns
import pandas as pd

#       Create a List of Random number ...
dataset_size = 1000

# --Unifom Random number generate...
uniform_nums = np.random.uniform(low=0.0, high=10.0, size=dataset_size)

# --Normal Random number generate
normal_nums = np.random.normal(loc=10, scale=20, size=dataset_size)

###         Print Dataset
#       print(uniform_nums)


###     --Createing plot...
def randomNum_plot(dataset, title):
    sns.histplot(dataset, bins=30, kde=False)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title(title)
    sns.despine(offset=10, trim=True)

    pass


###         RESULTS
#       --mean result...
print("Mean Result   : \n", normal_nums.mean(), "\n", uniform_nums.mean(), "\n")

#       --Median Result...
print("Median Result   : \n", np.median(normal_nums), "\n", np.median(uniform_nums))

#       --Variance Result   -^2
print("\n\n Normal Variance Result : ", np.var(normal_nums))
print(" Uniform Variance Result : ", np.var(uniform_nums))

#       --Standard Deviation --
print("\n\n Normal STD Result : ", np.std(normal_nums))
print(" Uniform STD Result : ", np.std(uniform_nums))

###     --Display Graph
plt.figure(figsize=(20, 6))
plt.subplot(1, 2, 1)
randomNum_plot(normal_nums, "Normal Random Value!")
plt.subplot(1, 2, 2)
randomNum_plot(uniform_nums, "Uniform Random Value!")

plt.tight_layout()
plt.show()
