from datasets import load_dataset
import pandas as pd

# Cargar el dataset
dataset = load_dataset("mstz/heart_failure")

# Obtener los datos de entrenamiento
data = dataset["train"]

# Convertir el Dataset en un DataFrame de Pandas
df = pd.DataFrame(data)

# Separar el DataFrame en dos, uno con las filas de personas que perecieron (is_dead=1) y otro con el complemento
df_perecidos = df[df["is_dead"] == 1]
df_no_perecidos = df[df["is_dead"] == 0]

# Calcular el promedio de las edades de cada dataset
promedio_edad_perecidos = df_perecidos["age"].mean()
promedio_edad_no_perecidos = df_no_perecidos["age"].mean()

# Imprimir los promedios de las edades
print("Promedio de edad de personas que perecieron:", promedio_edad_perecidos)
print("Promedio de edad de personas que no perecieron:", promedio_edad_no_perecidos)
