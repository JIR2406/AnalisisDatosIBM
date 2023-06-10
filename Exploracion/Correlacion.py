# La correlacion es una metrica estadistica para medir hasta que puntos las diferentes variables son interdependientes

# Metodos estadisticos de correlacion:

"""
Correlacion de Pearson:
Te dara dos valores, el coeficiente de correlacion y el valor P
Para el coeficiente de correlacion, un valor cercano a 1 implica una gran correlacion positiva.
mientras que un valor cernano a 1 negativo implica una correlacion negativa
Un valor cercano a 0 implica que no hay correlacion entre las variables
"""

# El valor P nos dira lo seguros que estamos de la correlacion que hemos calculado

"""
Para P un valor inferior a 0,001 nos da una fuerte certeza sobre el coeficiente de correlacion que hemos calculado
Un valor entre 0,001 y 0,05 nos da una certeza moderada
Un valor entre 0,05 y 0,1 nos dara una certeza debil
Y un valor mayor que 0,1 no nos dara ninguna certeza de correlacion
"""

# Podemos decir que hay una fuerte correlacion cuando el coeficiente es cercano a 1 o -1
# y el valor P es menor que 0,001

# paquete: SI/PI


"""
Analisis de varianza ANOVA

ANOVA: Es una prueba estadistica que significa Analisis de Varianza
Se utiliza para encontrar la correlacion entre los diferentes grupos de una variable categorica

Devuelve dos valores el test F y el valor P

El test F calcula el radio de variacion entre la media de los grupos sobre la variacion en cada uno de los grupos de muestra

El valor p muestra si el resultado obtenido es estadisticamente significativo
"""