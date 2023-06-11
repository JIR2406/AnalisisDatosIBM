import seaborn as sns
from pandas import DataFrame as df

sns.residplot(df['dependiente'],df['independiente'])

"""
Para medir el MSE averiguamos la diferencia entre el valor real y y el valor 
pronostico y sobrero y luego lo elevamos al cuadrado

Para encontrar el MSE de Python podemos importar mean_Squared_error

La funcion recive dos entradas, el valor real de la variable objetivo y el valor predicho de la 
variable objetivo


"""

"""
R-Cuadrado:

Tambien se llama coeficiente de determinacion, es una medida para determinar lo cerca que estan los datos de la linea
de regresion ajustada


"""
