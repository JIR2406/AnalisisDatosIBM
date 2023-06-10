class practica:
    import pandas as pd
    def __init__(self,ruta): # Tenemos que mandar la ruta del CSV
        self.__ruta=ruta
        self.df = self.pd.read_csv(self.__ruta,header=None) # Leemos el documento
    
    def guardarArchivo(self,ruta):
        self.df.to_csv(ruta+".csv",index=False) # Agregamos ruta y nombre del archivo C:/Users/jairg/OneDrive/Documentos/Documentos Analisis/nombre
    
    
if __name__=="__main__":
    pc=practica("https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv") # Objeto y ruta
    headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"] # Tenemos que crear una lista con los nombres de las columnas
    pc.df.columns=headers # Agregamos un encabezado
    pc.df.dropna(subset=["price"],axis=0) # Eliminamos datos faltantes
    #print(pc.df.dtypes) # Este nos permite ver los tipos de datos que tienen
    #print(pc.df.columns) # Muestra el nombre de las columnas
    #print(pc.df.describe(include="all")) # Resumen estatico de cada columna
    print(pc.df[['length', 'compression-ratio']].describe()) # Esto es para especificar las columnas
    #print(pc.df.info) # Muestra una informacion general sobre el dataFrame
    
    #print(pc.df)
    
    
    #print(pc.df.tail(10)) # 10 ultimas filas
    #print(pc.df.head(10)) # 10 primeras filas