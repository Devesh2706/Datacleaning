import csv
import pandas as pd

df = pd.read_csv("total_stars.csv")

del df["Star_name.1"]
del df["Distance.1"]
del df["Mass.1"]
del df["Radius.1"]
del df["Luminosity"]

print (list(df))
print (df.shape)
df.to_csv("final.csv")
