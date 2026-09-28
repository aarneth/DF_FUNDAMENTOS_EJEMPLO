# main.py (Fragmento actualizado)
import recepcion
import ventanilla
import consultas
import archivos

def mostrar_menu():
    print("\n" + "="*50)
    print("  MESA DE PARTES DIGITAL - SAN JUAN DE LURIGANCHO")
    print("="*50)
    print("1. Registrar nuevo trámite (Recepción)")
    print("2. Atender ciudadano (Ventanilla)")
    print("3. Consultar estado de trámite (Búsqueda)")
    print("4. Reporte de expedientes (Ordenamiento)")
    print("5. Salir del sistema")
    print("==================================================")

def main():
    expedientes = [] 
    archivos.cargar_expedientes(expedientes)
    continuar = True

    while continuar:
        mostrar_menu()
        opcion = input("Ingrese una opción (1-5): ")

        if opcion == '1':
            recepcion.registrar_expediente(expedientes)
            archivos.guardar_expedientes(expedientes)
        elif opcion == '2':
            ventanilla.atender_ciudadano(expedientes)
        elif opcion == '3':
            consultas.consultar_estado(expedientes)
        elif opcion == '4':
            consultas.mostrar_reporte_ordenado(expedientes) # <--- Requisito de Ordenamiento
        elif opcion == '5':
            print("\nGuardando datos finales...")
            archivos.guardar_expedientes(expedientes)
            print("Saliendo del sistema. ¡Hasta luego!")
            continuar = False
        else:
            print("\nError: Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()