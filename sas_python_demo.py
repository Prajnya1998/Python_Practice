import pandas as pd 

df = pd.read_csv("Global_Superstore_100.csv")

print(df.head())

print("Rows and Columns")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nInformation:")
print(df.info())

technology_data = df[df["Category"]=="Technology"]

print(technology_data.head())

technology_data.to_csv("technology_sales.csv", index=False)
