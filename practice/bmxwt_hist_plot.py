import pandas as pd
import matplotlib.pylab as plt
from collections import Counter

url = "data/nhanes_2015_2016.csv"
da = pd.read_csv(url)

if da is None:
    raise FileExistsError("Data set not found!")

#   shape using histogram...

weights = da["BMXWT"]  #   BMXWT data Info
print(weights, "\n")
print(weights.mean())  # ----average mean

print(weights.value_counts())

cont = Counter()
for size in weights:
    cont[size] += 1

cont.most_common()


# -------------Histogram representation...
plt.hist(weights, bins=30)
plt.xlabel("weights")
plt.ylabel("Frequency")
plt.title("Histogram representation of weights")
plt.grid()
plt.show()
