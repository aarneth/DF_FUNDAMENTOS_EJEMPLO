# recepcion.py

def generar_codigo(lista_expedientes):
    # Genera un código simple basado en la cantidad de registros actuales
    numero = len(lista_expedientes) + 1
    return f"T-{numero:03d}"

def registrar_expediente(expedientes):
    print("\n--- NUEVO REGISTRO DE TRÁMITE ---")
    
    # Validación de DNI (Tema 4: Cadenas y Tema 1: Condicionales/Bucles)
    dni_valido = False
    while not dni_valido:
        dni = input("Ingrese el número de DNI (8 dígitos): ").strip()
        if len(dni) == 8 and dni.isdigit():
            dni_valido = True
        else:
            print("Error: El DNI debe contener exactamente 8 números.")

    # Validación de campos vacíos
    campos_llenos = False
    while not campos_llenos:
        nombres = input("Ingrese Nombres completos: ").strip()
        apellidos = input("Ingrese Apellidos completos: ").strip()
        tramite = input("Ingrese el tipo de trámite (Ej. Licencia, Queja, Pago): ").strip()

        if len(nombres) > 0 and len(apellidos) > 0 and len(tramite) > 0:
            campos_llenos = True
        else:
            print("Error: Ningún campo puede estar vacío. Vuelva a ingresarlos.")

    # Generar código y estructurar el registro para agregarlo a la lista
    codigo = generar_codigo(expedientes)
    
    # Convertimos los textos a mayúsculas para mantener uniformidad (Tema 4)
    nuevo_registro = {
        "codigo": codigo,
        "dni": dni,
        "nombres": nombres.upper(),
        "apellidos": apellidos.upper(),
        "tramite": tramite.upper(),
        "estado": "Pendiente de Atención"
    }

    expedientes.append(nuevo_registro)

    print("\n==================================")
    print("¡Registro exitoso!")
    print(f"Su código de ticket es: {codigo}")
    print("Por favor, espere su turno en ventanilla.")
    print("==================================")