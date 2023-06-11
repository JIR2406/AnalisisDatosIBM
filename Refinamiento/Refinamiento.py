
# La evaluacion de modelo nos dice como se comporta nuestro modelo en el mundo real

"""
El error de generalizacion es una medida de lo bien que nuestros datos
predicen datos que no se han visto anteriormente

El error que obtenemos usando nuestros datos de prueba es una aproximacion de este error

Una de las metricas de evaluacion de muestra mas comunes es la validacion cruzada
el conjunto de datos se divide en K grupos iguales cada grupo se denomina parte fold

La forma mas sencilla de aplicar la validacion cruzada es llamar a la funcion
cross_val_score, que realiza multiples evaluaciones fuera de la muestra

Esta funcion devuelve un valor de puntuacion para indicarnos el resultado de la validacion cruzada

"""


"""
La regresion de arista previene el sobreajuste 

Grind Search nos permite explorar a traves de multiples parametros libres con unas pocas lineas
de codigo

Toma el modelo o los objetos que deseas entrena y diferentes valores de los 
hiperparametros

Luego clacula el error cuadratico medio o R-cuadrado para varios valores de hiperparametros lo que 
te permite elegir los mejores valores


"""