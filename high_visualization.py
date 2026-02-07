import pandas as pd
df = pd.read_csv(r"C:\Users\abdul\OneDrive\Documents\world-population.csv")
print(df[["Continent"]].value_counts())
