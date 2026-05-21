import requests
import ctypes

# se define la URL de la API
url_api = "https://api.worldbank.org/v2/en/country/all/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1&country=%22Argentina%22"

# request y JSON
respuesta = requests.get(url_api)
datos = respuesta.json()

# se aisla la lista de registros (posicion 1)
lista_registros = datos[1]

# variable donde se almacena el indice de Gini de Argentina
gini_argentina = None

# iteración para filtrar
for registro in lista_registros:
    nombre_pais = registro['country']['value']
    valor_gini = registro['value']
    
    if nombre_pais == "Argentina" and valor_gini is not None:
        gini_argentina = valor_gini
        break

# se muestra el valor
print(f"El índice de Gini para Argentina es: {gini_argentina}")

# se carga la librería de C
lib_c = ctypes.CDLL('./libgini.so')

# se declaran los tipos de datos  
lib_c.calcular_gini.argtypes = [ctypes.c_float]
lib_c.calcular_gini.restype = ctypes.c_int

# se ejecuta la funcion de C (se obtiene el Gini de Argentina tipo int)
resultado_final = lib_c.calcular_gini(gini_argentina)

# se muestra el valor
print(f"El valor final es: {resultado_final}")
