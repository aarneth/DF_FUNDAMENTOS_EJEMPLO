# consultas.py

def consultar_estado(expedientes):
    print("\n--- CONSULTA DE ESTADO DE TRÁMITE ---")
    parametro = input("Ingrese su número de Ticket (Ej. T-001) o DNI para buscar: ").strip().upper()
    
    encontrado = False
    
    # Algoritmo de búsqueda lineal (Tema 3)
    for exp in expedientes:
        if exp["codigo"] == parametro or exp["dni"] == parametro:
            print("\n=== RESULTADO ENCONTRADO ===")
            print(f"Ticket: {exp['codigo']}")
            print(f"Ciudadano: {exp['nombres']} {exp['apellidos']}")
            print(f"Trámite: {exp['tramite']}")
            print(f"ESTADO ACTUAL: {exp['estado']}")
            print("============================")
            encontrado = True
            
    if not encontrado:
        print(f"No se encontraron trámites registrados con el valor: {parametro}")

def mostrar_reporte_ordenado(expedientes):
    print("\n--- REPORTE: EXPEDIENTES ORDENADOS POR APELLIDO ---")
    
    if len(expedientes) == 0:
        print("No hay expedientes registrados.")
        return

    # Creamos una copia para no alterar el orden original de atención de la cola
    lista_ordenada = expedientes.copy()
    n = len(lista_ordenada)
    
    # Algoritmo de ordenamiento de la Burbuja (Bubble Sort - Requisito del Tema 3)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Comparamos alfabéticamente los apellidos
            if lista_ordenada[j]['apellidos'] > lista_ordenada[j + 1]['apellidos']:
                # Intercambiamos las posiciones
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]
                
    # Mostramos los resultados ordenados
    for exp in lista_ordenada:
        print(f"[{exp['codigo']}] {exp['apellidos']}, {exp['nombres']} - Estado: {exp['estado']}")
    print("===================================================")