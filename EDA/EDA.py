#%%
import pandas as pd

df = pd.read_excel("C. Base de dados.xlsx")
df.head()
# %%
df.info()
# %%
df.isnull().sum()
# %%
df["Data_Admissao"] = pd.to_datetime(df["Data_Admissao"])
df["Data_Saida"] = pd.to_datetime(df["Data_Saida"])
df.head(1)
# %%
df.describe()
# %%
df.groupby("Departamento").size()
# %%
df_Marketing = df[df["Departamento"] == "Marketing"]
df_Marketing.head()
# %%
df_Operacoes = df[df["Departamento"] == "Operações"]
df_Operacoes.head()
# %%
df_Vendas = df[df["Departamento"] == "Vendas"]
df_Vendas.head()
# %%
df_Tecnologia = df[df["Departamento"] == "Tecnologia"]
df_Tecnologia.head()
# %%
df_Operacoes = df[df["Departamento"] == "Operações"]
df_Operacoes.head()
# %%
df["Status"] = df["Data_Saida"].apply(lambda x: "Ativo" if pd.isnull(x) else "Inativo")
df.head()
# %%
df.to_excel("C. Base de dados - Tratada.xlsx", index=False)
df_Marketing.to_excel("C. Base de dados - Marketing.xlsx", index=False)
df_Operacoes.to_excel("C. Base de dados - Operações.xlsx", index=False)
df_Vendas.to_excel("C. Base de dados - Vendas.xlsx", index=False)
df_Tecnologia.to_excel("C. Base de dados - Tecnologia.xlsx", index=False)

# %%
