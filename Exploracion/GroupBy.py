# El metodo Groupby() se utiliza en variables categoricas
# agrupa los datos en subcojuntos de acuerdo con las diferentes categorias de esa variable
# se pueden agrupar por multiples variables pasando los multiples nombres de las variables

from pandas import DataFrame as df
df_test= df[['drive-wheels','body-style','prices']]
df_grp = df_test.groupby(['drive_wheels','body-style'],as_index=False).mean()
df_grp

# Una tabla dinamica tiene una variable que se muestra a lo largo
# de las columnas y otra variable que se muestra a lo largo de las filas.

df_pivot= df_grp.pivot(index='drive-wheels',columns='body-style')

# Grafico de mapa de calor: Toma una cuadricula rectangulas de datos y asigna
# una intensidad de color basada en el valor de los datos en los puntos de la cuadricula

