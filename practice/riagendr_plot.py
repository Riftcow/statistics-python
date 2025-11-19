import matplotlib.pylab as plt
import pandas as pd

#   import NHance dataset.

url = "data/nhanes_2015_2016.csv"
da = pd.read_csv(url)

if da is None:
    raise FileExistsError("data set not found!")

gender_nhanes = da["RIAGENDR"]
gender_values = gender_nhanes.value_counts()
print(gender_nhanes)

# ----   ploting the data...
gender_nhanes.value_counts().plot(kind="bar")
plt.xticks([0, 1], ["Male", "Female"])
plt.ylabel("Frequency")
plt.title("Gender Data Plot")
plt.show()
