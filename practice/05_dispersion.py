#       @FU4Y
#   Library import...

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import normal, uniform
import seaborn as sns
import pandas as pd

#       Create a List of Random number ...
dataset_size = 10000

# --Unifom Random number generate...
uniform_nums = np.random.uniform(low=0.0, high=10.0, size=dataset_size)

# --Normal Random number generate   --01    -SCALE 20
normal_nums = np.random.normal(loc=10, scale=20, size=dataset_size)

#   Normal Random number generate... -SCLAE 30
normal_nums2 = np.random.normal(loc=10, scale=30, size=dataset_size)


###         Print Dataset
# print(np.mean(normal_nums))


def SD_line_plot(
    x_val,
    y_val,
    custom_color: str,
):
    #   Plot Standard Deviation Line on Graph...
    x_c, y_c = ([x_val, y_val], [0, 2000])
    plt.plot(x_c, y_c, color=custom_color, linewidth=2)


pass


###     --Createing plot...
def randomNum_plot(data_set, title):

    #   important variables for Normal Values...
    normal_n_mean = np.mean(data_set)  #   average Mean for normal Values
    normal_n_sd = np.std(data_set)  # Standard Deviation for normal Values

    sns.histplot(data_set, bins=30, kde=False)
    plt.xlim(-100, 100)

    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title(title)
    sns.despine(offset=10, trim=True)

    # Draw a Line
    SD_line_plot(normal_n_mean, normal_n_mean, "Red")
    SD_line_plot((normal_n_mean + normal_n_sd), (normal_n_mean + normal_n_sd), "Green")
    SD_line_plot((normal_n_mean - normal_n_sd), (normal_n_mean - normal_n_sd), "Green")


pass


###     --Display Graph
plt.figure(figsize=(30, 10))

plt.subplot(1, 2, 1)
randomNum_plot(normal_nums, "Normal Random Value!")

plt.subplot(1, 2, 2)
randomNum_plot(normal_nums2, "Normal Random Value 2!")

plt.tight_layout()
plt.show()
