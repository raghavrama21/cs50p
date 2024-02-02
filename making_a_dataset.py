import pandas as pd

a = [1,2,3]
b = ["A","B","C"]

pd.DataFrame([a,b]).to_csv(r"test.csv")

