import pandas as pd

#       consider a DataFrame we gave...
Box = ["bird", "cat", "dog", "bird", "dog", "dog", "cat", "bird"]
data = {"Categorical": Box}

#   Convert to DataFrame
df = pd.DataFrame(data)

#    basic value test display...
print(df[pd.Categorical], "\n")
print(df.nunique(), "\n")

# ---1 Hot Vector Encoding
df_dummies = pd.get_dummies(df["Categorical"], prefix="Category!")

print(df_dummies)  #   Vector Table
print("\n", df_dummies.values.astype(int))
