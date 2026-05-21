import requests
import ctypes

# python entra a la api y extrae el gini
url_api = "https://api.worldbank.org/v2/en/country/all/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1&country=%22Argentina%22"

respuesta = requests.get(url_api)
datos = respuesta.json()
lista_registros = datos[1]

gini_argentina = None

for registro in lista_registros:
    if registro['country']['value'] == "Argentina" and registro['value'] is not None:
        gini_argentina = registro['value']
        break

# se crea la comunicacion entre py y c
lib_c = ctypes.CDLL('./libgini.so')

lib_c.calcular_gini.argtypes = [ctypes.c_float]
lib_c.calcular_gini.restype = ctypes.c_int

resultado_final = lib_c.calcular_gini(gini_argentina)

print(f"El índice de Gini de Argentina es: {resultado_final}")