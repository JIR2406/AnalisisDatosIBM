"""
La exploracion de datos o abreviado EDA
es un enfoque para analizar datos con el fin de 
resumir las principales caracteristicas de los datos
obtener una mejor compresion del conjunto de datos,
descubrir las relaciones entre las diferentes variables,
y extraer las variabñes importantes para el problema que estamos
tratando de resolver.
"""

# Estadistica descriptiva

# Ayuda a describir las caracteristicas basicas de un conjunto de datos 
# y obtiene un breve resumen sobre la muestra y las mediciones de los datos

import pandas as pd
"""
import matplotlib as plt
df.describe() # Describe automaricamente las estadisticas basicas de todas las variables numericas

df.value_counts() # Variables categoricas en el conjunto de datos


y=df["price"]
x=df["egine-size"]
plt.scatter(x,y)

plt.title("Scanner")
plt.xlabel("Engine Size")
plt.ylabel("Price")

"""
df1=pd.DataFrame({'A':["a","b","a","c","a","c","b"]})
print(df1['A'].value_counts())