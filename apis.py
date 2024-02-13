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
        else:
            print(
                f"Error al descargar los datos. Código de estado: {respuesta.status_code}"
            )
    except Exception as e:
        print(f"Error durante la descarga de datos: {e}")


# URL de los datos
url_datos = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"

# Nombre del archivo CSV donde se guardará la respuesta
nombre_archivo_csv = "datos_descargados.csv"

# Llamar a la función para descargar los datos
descargar_datos_csv(url_datos, nombre_archivo_csv)
