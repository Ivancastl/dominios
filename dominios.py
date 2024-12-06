import requests
import re
from datetime import datetime, timedelta
import pyfiglet  # Librería para generar texto en arte ASCII
import os


def mostrar_etiqueta():
    # Generar arte ASCII para "dominios"
    texto_ascii = pyfiglet.figlet_format("dominios")
    print(texto_ascii)


def pedir_palabras_clave():
    # Solicitar palabras clave o "todo" al usuario
    palabras_clave = input("Ingresa las palabras clave separadas por comas o escribe 'todo' para buscar todo: ").strip()
    if not palabras_clave:
        print("No se especificaron palabras clave. Por favor, inténtalo de nuevo.")
        return pedir_palabras_clave()
    if palabras_clave.lower() == "todo":
        return []
    else:
        return [palabra.strip() for palabra in palabras_clave.split(",")]


def pedir_rango_fechas():
    while True:
        rango = input(
            "Ingresa una fecha (YYYYMMDD) o un rango de fechas (YYYYMMDD-YYYYMMDD): "
        ).strip()
        try:
            if "-" in rango:
                fecha_inicio_str, fecha_fin_str = rango.split("-")
                fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y%m%d")
                fecha_fin = datetime.strptime(fecha_fin_str, "%Y%m%d")
                if fecha_inicio > fecha_fin:
                    print("La fecha de inicio no puede ser posterior a la fecha final. Intenta de nuevo.")
                else:
                    return fecha_inicio, fecha_fin
            else:
                fecha_unica = datetime.strptime(rango, "%Y%m%d")
                return fecha_unica, fecha_unica
        except ValueError:
            print("Formato inválido. Asegúrate de usar el formato YYYYMMDD o YYYYMMDD-YYYYMMDD.")


def generar_fechas_rango(fecha_inicio, fecha_fin):
    fecha_actual = fecha_inicio
    fechas = []
    while fecha_actual <= fecha_fin:
        fechas.append(fecha_actual.strftime("%Y-%m-%d"))
        fecha_actual += timedelta(days=1)
    return fechas


def descargar_archivo(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"No se pudo descargar el archivo desde: {url}")
        return None


def buscar_palabra_clave(texto, palabras_clave):
    lineas = texto.splitlines()
    if not palabras_clave:  # Si la lista está vacía, devolver todas las líneas
        return lineas
    coincidencias = []
    for palabra in palabras_clave:
        coincidencias.extend([linea for linea in lineas if re.search(r'\b' + re.escape(palabra) + r'\b', linea, re.IGNORECASE)])
    return coincidencias


def buscar_en_dias(palabras_clave, fechas):
    ruta_actual = os.getcwd()  # Obtener carpeta actual
    archivo_salida_path = os.path.join(ruta_actual, "coincidencias.txt")
    with open(archivo_salida_path, "w") as archivo_salida:
        for fecha in fechas:
            url = f"https://raw.githubusercontent.com/nicotechtips/nitt-sec-nrd/main/lists/{fecha}.txt"
            print(f"Buscando en: {url}")
            archivo_contenido = descargar_archivo(url)
            if archivo_contenido:
                coincidencias = buscar_palabra_clave(archivo_contenido, palabras_clave)
                if coincidencias:
                    archivo_salida.write(f"Coincidencias en {fecha}:\n")
                    for coincidencia in coincidencias:
                        archivo_salida.write(coincidencia + "\n")
                    archivo_salida.write("\n")
                else:
                    archivo_salida.write(f"No se encontraron coincidencias en {fecha}.\n\n")
    print(f"Resultados guardados en: {archivo_salida_path}")


if __name__ == "__main__":
    mostrar_etiqueta()
    palabras_clave = pedir_palabras_clave()
    fecha_inicio, fecha_fin = pedir_rango_fechas()
    fechas = generar_fechas_rango(fecha_inicio, fecha_fin)
    buscar_en_dias(palabras_clave, fechas)
    print("Búsqueda completada.")
