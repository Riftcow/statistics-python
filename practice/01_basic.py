import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

url = "data/nhanes_2015_2016.csv"
da = pd.read_csv(url)

#   display the head of DataFrame
#       print(da.head())

# print the shape of Dataframe
print(da.shape)

#   show the Columns variable of DataFrame

print("\n", da.columns)

#   show specific column

print("\n", da["BMXWT"])
print("\n", da["BMXWT"].size)

#   now to visuvalize the Data in the Histogram Plotting Order

plt.figure(figsize=(24, 8))

x_value = range(da["BMXWT"].size)
y_value = da["BMXWT"]

#   plot data
plt.scatter(x_value, y_value, marker="x", s=0.4)
#   plt.plot(x_value, y_value)

plt.title("Weight of a Person")
plt.xlabel("Weight")
plt.ylabel("Person")

plt.show()

#   average finding...
#       y_value = y_value.dropna()
print("\n\n", sum(y_value) / len(y_value))

# create a pdf file

# Create PDF file
with PdfPages("nhanes_report.pdf") as pdf:
    # ---------- PAGE 1 : DataFrame Info ----------
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.axis("off")

    # Prepare text summary
    summary = []
    summary.append(f"Shape of DataFrame: {da.shape}")
    summary.append("\nColumns:")
    summary.append(", ".join(da.columns))
    summary.append("\n\nFirst 5 Rows:\n")
    summary.append(da.head().to_string())
    summary.append("\n\n Average of BMXWT Data : \n")
    temp = y_value.dropna()
    summary.append(sum(temp) / len(y_value))
    ax.text(
        0,
        1,
        "\n".join(map(str, summary)),
        fontsize=10,
        va="top",
        ha="left",
        family="monospace",
    )
    pdf.savefig(fig)
    plt.close(fig)

    # ---------- PAGE 2 : Scatter Plot ----------
    fig, ax = plt.subplots(figsize=(14, 6))

    x_value = range(da["BMXWT"].size)
    y_value = da["BMXWT"]

    ax.scatter(x_value, y_value, marker="x", s=0.4)
    ax.set_title("Weight of a Person")
    ax.set_xlabel("Index (Person)")
    ax.set_ylabel("Weight")

    pdf.savefig(fig)
    plt.close(fig)
