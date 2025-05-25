import pandas as pd

NAMES = ["BLUE", "BLACK"]

df = pd.read_excel("data.xlsx")
df = df.fillna(0)
df[['M', 'S', 'R']] = df[['M', 'S', 'R']].astype(int)

filtered_df = df[df["NAME"].isin(NAMES)]

filtered_df.to_excel("output.xlsx", index=False)