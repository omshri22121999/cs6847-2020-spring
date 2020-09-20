import pandas as pd
import sys

data = pd.read_csv(sys.argv[1], encoding= 'unicode_escape')
data["StockCode"] = data["StockCode"].astype(str)

nan_value = float("NaN")
data.replace("", nan_value, inplace=True)
data.dropna(inplace=True)

groups_inv = data.groupby("InvoiceNo")["StockCode"]
invoices = set(data["InvoiceNo"])
out_list = []
for i in invoices:
    out_list.append(list(groups_inv.get_group(i)))
with open("FP_Part-2_changed.csv","w") as f:
    for i in out_list:
        f.write(','.join(i)+"\n")

