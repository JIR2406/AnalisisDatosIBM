from pandas import DataFrame as df

df.dropna(subset="price",axis=0) # Borrar datos nulos

# df.replace(missing_value,new_value)