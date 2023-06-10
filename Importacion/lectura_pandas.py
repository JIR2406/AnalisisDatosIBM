import pandas as pd
# read the online file by the URL provided above, and assign it to variable "df"
path="C:/Users/jairg/OneDrive/Documentos/GitHub/Proyectos_basicos_R/Semana 3/flavors_of_cacao.csv"

df = pd.read_csv(path,header=None)

# df.head(n) Muestra las primeras columnas del frame
# df.tail(n) Muestra las ultimas columnas del frame
print(df.head(5))

# Podemos guardar otro archivo csv

# path = "ruta/.nombrearchivo.csv"
# df.to_csv(path)

print(df.describe(include="all"))
print(df.info())