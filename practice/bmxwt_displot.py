import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

url = "data/nhanes_2015_2016.csv"
da = pd.read_csv(url)

if da is None:
    raise FileExistsError("File not Found!")

weights = da["BMXWT"]

print(weights.mode())  #   mode representation
print(weights.mean())  #   mean representation

sns.distplot(weights, bins=25, kde=True)
plt.grid()
plt.xlabel("Weights Level")
plt.ylabel(" Individuals ", labelpad=None)

plt.show()
