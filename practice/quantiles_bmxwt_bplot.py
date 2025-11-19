import pandas as pd
import matplotlib.pylab as plt
import statistics
import seaborn as sns

url = "data/nhanes_2015_2016.csv"
da = pd.read_csv(url)

#   check for file avail?
if da is None:
    raise FileExistsError("File Not Found!")

#   --  organizing for var...
weight = da["BMXWT"]
gendr = da["RIAGENDR"]
health_insurance = da["HIQ210"]

statistics.quantiles(weight, n=4)
statistics.quantiles(gendr, n=4)
statistics.quantiles(health_insurance, n=4)

wt_male = da.loc[da["RIAGENDR"] == 2, "BMXWT"]
wt_female = da.loc[da["RIAGENDR"] == 1, "BMXWT"]

print(wt_male.mean())
print(wt_female.mean())


def boxplot_dataframe(x_mark, y_mark, data_frame, position, color_p, title):

    plt.subplot(1, 2, position)
    sns.boxplot(x=x_mark, y=y_mark, data=data_frame, palette=color_p)
    plt.title(title)

    pass


#   --  Data Plotting section!
plt.figure(figsize=(20, 4))
sns.set_style("whitegrid")

#   --Weight to Gender
boxplot_dataframe("RIAGENDR", "BMXWT", da, 1, "Set3", "Weight To Gender Ratio")
#   --   Weight to health Insurance
boxplot_dataframe("HIQ210", "BMXWT", da, 2, "Set3", "Weight to Health Insurance Ratio")
plt.show()
