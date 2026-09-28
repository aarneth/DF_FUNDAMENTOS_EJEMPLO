# archivos.py
import os

ARCHIVO_DATOS = "expedientes.txt"

def cargar_expedientes(expedientes):
    """Carga los datos del archivo de texto a la memoria (lista) al iniciar el programa."""
    if not os.path.exists(ARCHIVO_DATOS):
        # Si el archivo no existe, lo crea vacío
        with open(ARCHIVO_DATOS, 'w') as file:
            pass
        return

    # Si existe, lee los registros y los añade a la lista
    with open(ARCHIVO_DATOS, 'r') as file:
        lineas = file.readlines()
        for linea in lineas:
            datos = linea.strip().split("|")
            if len(datos) == 6:
                registro = {
                    "codigo": datos[0],
                    "dni": datos[1],
                    "nombres": datos[2],
                    "apellidos": datos[3],
                    "tramite": datos[4],
                    "estado": datos[5]
                }
                expedientes.append(registro)

def guardar_expedientes(expedientes):
    """Sobrescribe el archivo con la lista actual de expedientes."""
    with open(ARCHIVO_DATOS, 'w') as file:
        for exp in expedientes:
            linea = f"{exp['codigo']}|{exp['dni']}|{exp['nombres']}|{exp['apellidos']}|{exp['tramite']}|{exp['estado']}\n"
            file.write(linea)