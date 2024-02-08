from datasets import load_dataset
import numpy as np

# cargar el data dataset
dataset = load_dataset("mstz/heart_failure")
# obtener los datos de entrenamiento
data = dataset["train"]

# obtener la lista de edades
ages = data["age"]

# convertir la lista de edades a un arreglo de Numpy
ages_array = np.array(ages)

# Calcular el promedio
average_age = np.mean(ages_array)

print(
    "El promedio de edad de las personas participantes en el estudio es:", average_age
)
