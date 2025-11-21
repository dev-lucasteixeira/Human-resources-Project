#%%
import pandas as pd

EXCEL_FILE = "C. Base de dados - Tratada.xlsx"

df = pd.read_excel(EXCEL_FILE)

df.to_csv("C. Base de dados - Tratada.csv", index=False)
# %%
