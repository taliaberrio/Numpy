from datasets import load_dataset
import pandas as pd

# Cargar el dataset
dataset = load_dataset("mstz/heart_failure")

# Obtener los datos de entrenamiento
data = dataset["train"]

# Convertir el dataset a un DataFrame de pandas
df = pd.DataFrame(data)

# Verificar los tipos de datos en cada columna
tipos_de_datos = df.dtypes
print("Tipos de datos en cada columna:")
print(tipos_de_datos)

# Calcular la cantidad de hombres fumadores vs mujeres fumadoras
cantidad_hombres_fumadores = df[
    (df["is_male"] == True) & (df["is_smoker"] == True)
].shape[0]
cantidad_mujeres_fumadoras = df[
    (df["is_male"] == False) & (df["is_smoker"] == True)
].shape[0]

print("\nCantidad de hombres fumadores:", cantidad_hombres_fumadores)
print("Cantidad de mujeres fumadoras:", cantidad_mujeres_fumadoras)
