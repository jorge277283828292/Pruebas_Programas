import pandas as pd

edades = pd.Series([20, 25, 30])
print(edades) #Una lista con un indice numerico

print()

datos = {
    "Nombre": ["Jorge", "Ana", "Luis"],
    "Edad": [25, 30, 28],
    "Ciudad": ["Madrid", "Barcelona", "Valencia"],
    "Calificacion": [85, 90, 95],
} #Tabla con dattos estructurados

df = pd.DataFrame(datos)
print(df) 

print()

dates = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=["A", "B", "C"])
print(dates) #DataFrame con datos no estructurados

