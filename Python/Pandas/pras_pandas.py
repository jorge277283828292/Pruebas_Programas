import pandas as pd
import xlrd
import matplotlib.pyplot as plt
import seaborn as sns

df_excl = pd.read_excel("C:/Users/jv748/Desktop/Python/Pandas/datos_prueba_pandas.xlsx")
print(df_excl) 
#df_excl['Edad'].plot()
#plt.show()
#df_json = pd.read_json("C:/Users/jv748/Desktop/Python/Pandas/productos.json")
# print(df_json)

#df_json.to_excel("C:/Users/jv748/Desktop/Python/Pandas/productos.xlsx", index=False)

#print(df_json[['nombre', 'categoria']])

#print(df_json[df_json['categoria'] == 'Pinatas'])

#print(df_excl.iloc[0:10, 0:3]) 