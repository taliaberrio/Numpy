import pandas as pd
import numpy as np
import requests


def descargar_datos_csv(url, nombre_archivo):
    try:
        # Realizar la solicitud GET para descargar los datos
        respuesta = requests.get(url)

        # Verificar si la solicitud fue exitosa
        if respuesta.status_code == 200:
            # Escribir la respuesta en un archivo CSV
            with open(nombre_archivo, "wb") as archivo:
                archivo.write(respuesta.content)
            print(f"Los datos han sido descargados exitosamente como {nombre_archivo}")
            return True
        else:
            print(
                f"Error al descargar los datos. Código de estado: {respuesta.status_code}"
            )
            return False
    except Exception as e:
        print(f"Error durante la descarga de datos: {e}")
        return False


def procesar_datos(df):
    # Verificar valores faltantes
    print("Valores faltantes por columna:")
    print(df.isnull().sum())

    # Verificar filas duplicadas
    print("\nFilas duplicadas:")
    print(df.duplicated().sum())

    # Verificar valores atípicos y eliminarlos
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    df_clean = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]

    # Crear columna de categoría de edad
    bins = [0, 12, 19, 39, 59, np.inf]
    labels = ["Niño", "Adolescente", "Jóvenes adulto", "Adulto", "Adulto mayor"]
    df_clean["Age_Category"] = pd.cut(df_clean["age"], bins=bins, labels=labels)

    return df_clean


def descargar_y_procesar_datos(url, nombre_archivo):
    if descargar_datos_csv(url, nombre_archivo):
        # Cargar el CSV en un DataFrame
        df = pd.read_csv(nombre_archivo)

        # Procesar los datos
        df_procesado = procesar_datos(df)

        # Guardar el resultado como CSV
        nombre_archivo_procesado = "datos_procesados.csv"
        df_procesado.to_csv(nombre_archivo_procesado, index=False)
        print(f"Datos procesados guardados como {nombre_archivo_procesado}")


# URL de los datos
url_datos = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"

# Nombre del archivo CSV donde se guardará la respuesta
nombre_archivo_csv = "datos_descargados.csv"

# Llamar a la función para descargar y procesar los datos
descargar_y_procesar_datos(url_datos, nombre_archivo_csv)
