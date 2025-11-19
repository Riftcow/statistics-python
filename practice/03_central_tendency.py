import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

url = "data/nhanes_2015_2016.csv"
da = pd.read_csv(url)

if da is None:
    raise FileExistsError("File Not found Check directory!")

    #   Learning the basic of Central Tendency...!
weight = da["BMXWT"]

print(range(weight.size))  # consider as X
print(weight)

#   make a Scatter Data Plot
plt.figure(figsize=(18, 6))

x_data = range(weight.size)
y_data = weight

plt.scatter(x_data, y_data, marker="x", s=2)
plt.xlabel("Weights Level")
plt.ylabel(" Individuals ")

#   making a central Line on the basis of finding mean
# point1 = (0, int(y_data.mean()))
# point2 = (6000, int(y_data.mean()))

point1 = [0, 6000]
point2 = [int(y_data.mean()), int(y_data.mean())]


x_central, y_central = point1, point2

plt.plot(
    x_central, y_central, color="red", linewidth=1
)  # drawing a central according to mean method
print("Mean Value to Weight : ", weight.mean())
#   Median Line draw Color Green --
point2 = [int(y_data.median()), int(y_data.median())]
plt.plot(x_central, point2, color="green", linewidth=1)
print("Median Value to Weight : ", weight.median())
plt.show()
