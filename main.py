
import pandas as pd

data = pd.read_excel("sales_data.xlsx")

print(data["Product ID"].value_counts())
