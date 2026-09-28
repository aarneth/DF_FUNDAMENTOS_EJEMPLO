# ventanilla.py
import archivos

def atender_ciudadano(expedientes):
    print("\n--- MÓDULO DE VENTANILLA ---")
    
    # Buscamos el primer expediente que esté "Pendiente de Atención"
    # (Aplicación de búsqueda en arreglos - Tema 3)
    expediente_actual = None
    for exp in expedientes:
        if exp["estado"] == "Pendiente de Atención":
            expediente_actual = exp
            break
            
    if not expediente_actual:
        print("No hay ciudadanos en espera de atención.")
        return

    # Se muestran los datos estructurados y legibles
    print("\n[Llamando a ciudadano...]")
    print(f"Ticket: {expediente_actual['codigo']}")
    print(f"DNI: {expediente_actual['dni']}")
    print(f"Ciudadano: {expediente_actual['nombres']} {expediente_actual['apellidos']}")
    print(f"Trámite: {expediente_actual['tramite']}")
    
    # Validación del trabajador
    accion_valida = False
    while not accion_valida:
        print("\n¿Qué acción desea tomar?")
        print("1. Aprobar expediente")
        print("2. Observar/Rechazar expediente")
        opcion = input("Ingrese opción (1-2): ").strip()
        
        if opcion == '1':
            expediente_actual["estado"] = "Aprobado - En proceso de respuesta (30 días)"
            accion_valida = True
        elif opcion == '2':
            motivo = input("Ingrese el motivo de la observación: ").strip()
            expediente_actual["estado"] = f"Observado: {motivo.upper()}"
            accion_valida = True
        else:
            print("Error: Opción inválida.")
            
    # Guardamos inmediatamente en el archivo tras la atención (Tema 5)
    archivos.guardar_expedientes(expedientes)
    print("\nExpediente procesado y guardado correctamente.")