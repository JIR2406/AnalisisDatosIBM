import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

path='https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
df = pd.read_csv(path)

df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr()  

# Tamaño del motor como posible variable de predicción del precio
sns.regplot(x="engine-size", y="price", data=df)
plt.ylim(0,)

print(df[["engine-size", "price"]].corr())
sns.regplot(x="highway-mpg", y="price", data=df)
