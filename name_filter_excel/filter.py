import pandas as pd
import os

os.chdir(os.path.dirname(__file__))

def filter_names(input_file, output_file, names, columns):
  if "NAME" not in columns:
    columns.insert(0, "NAME")

  df = pd.read_excel(input_file)
  df = df.fillna(0)
  df = df[columns]
  filtered_df = df[df["NAME"].isin(names)]
  filtered_df.to_excel(output_file, index=False)

input_file = "data.xlsx"
output_file = "output.xlsx"
names = ["BLUE", "BLACK"]
columns = ["M", "CODE"]
filter_names(input_file, output_file, names, columns)