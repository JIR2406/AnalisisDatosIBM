import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import make_pipeline


file_name='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/coursera/project/kc_house_data_NaN.csv'
df=pd.read_csv(file_name).dropna

# print(df.head())
#print(df.dtypes)
###
#df.drop('id', axis=1, inplace=True)
#df.drop('Unnamed: 0', axis=1, inplace=True)
#print(df.describe())
###



#conteos=df['floors'].value_counts().to_frame()
#print(conteos)

# Definir las características y la variable objetivo
# Definir las características y la variable objetivo
features = ["floors", "waterfront", "lat", "bedrooms", "sqft_basement", "view", "bathrooms", "sqft_living15", "sqft_above", "grade", "sqft_living"]
X = df[features]
y = df['price']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el objeto de transformación polinomial de segundo orden
poly_transform = PolynomialFeatures(degree=2, include_bias=False)

# Crear el objeto de regresión de Ridge
ridge_model = Ridge(alpha=0.1)

# Crear el objeto de pipeline que incluye la transformación polinomial y el modelo de regresión de Ridge
pipeline = make_pipeline(poly_transform, ridge_model)

# Ajustar el pipeline a los datos de entrenamiento
pipeline.fit(X_train, y_train)

# Realizar las predicciones en los datos de prueba
y_pred = pipeline.predict(X_test)

# Calcular el coeficiente de determinación R^2
r2 = r2_score(y_test, y_pred)

print("Coeficiente de determinación R^2:", r2)