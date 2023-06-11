"""
Se puede pensar en un modelo o estimador como una ecuacion matematica utilizada para
predecir el valor dado uno o mas valores relacionando una o mas variables o caracteristicas independientes
con variables dependientes
"""
# Regreson lineal simple

"""
La regresion lineal se refiere a una variable independiente para hacer una prediccion
La regresion lineal multiple se refiere a multiples variables independientes para hacer una prediccion


La regresion lineal simple o RLS es un metodo que nos ayuda a entender la relacion entre dos variables
la variable independiente predictora x y la variable dependiente objetivo y

Los valores que intentamos predecir se llaman objetivo y lo almacenamos en array Y



from pandas import DataFrame as df
from sklearn.linear_model import LinearRegression 

lm=LinearRegression()
X = df[['highway-mpg']]
Y = df['price']

Su salida es un array tiene el mismo numero de muestras que la entrada x

La regresion lineal multiple se utiliza para explicar la relacion entre una variable continua objetivo
y  y dos o mas variables predictoras x
"""
from sklearn.linear_model import LinearRegression 
lm=LinearRegression()
X = df[['highway-mpg']]
Y = df['price']
lm.fit(X, Y)
Yhat=lm.predict(X)