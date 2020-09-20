import pandas as pd

data = pd.read_csv("summary.csv")

data_true = data[data["responseMessage"].eq("OK")]

data_true.to_csv("summary_hits.csv")
