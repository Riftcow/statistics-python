import pandas as pd
import matplotlib.pylab as plt
import numpy as np

# ---read data from csv file
url = "data/nhanes_2015_2016.csv"
da = pd.read_csv(url)


if da is None:
    raise FileExistsError("File not found in directory!\n")

#       print(da.column)
print(f"Average weights of 2015-2016 individuals :  {da["BMXWT"].mean()}\n")

# ---------------now dealing with Catigorical data..."DMDEDUC2"
#   print(da["DMDEDUC2"])
print(da["DMDEDUC2"].unique())  # show Catigorical order.
print(da["DMDEDUC2"], "\n")

# ---------------now dealing with Catigorical Unordered data..."RIAGENDR"
print(da["RIAGENDR"].unique())
print(da["RIAGENDR"], "\n")

# ----Exploring Unordered Catigorical data ... "RIAGENDR"
gendr = da["RIAGENDR"]

gendr = pd.get_dummies(gendr, prefix="RIAGENDR_1HOT")

print(gendr.values.astype(int))
