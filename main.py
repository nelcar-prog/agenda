
def eliminar_contacto(contactos):
    print("\n--- Eliminar Contacto ---")
    if not contactos:
        print("No hay contactos para eliminar.")
        return
    nombre_eliminar = input("Ingrese el nombre del contacto a eliminar: ").lower()
    cantidad_inicial = len(contactos)
    # Se crea una nueva lista excluyendo los contactos a eliminar
    contactos[:] = [contacto for contacto in contactos if nombre_eliminar not in contacto['nombre'].lower()]
    if len(contactos) < cantidad_inicial:
        print("Contacto(s) eliminado(s) exitosamente.")
    else:
        print("No se encontró ningún contacto con ese nombre para eliminar.")

    
=======
from functions import agregar_contacto, listar_contactos, buscar_contacto, eliminar_contacto, mostrar_menu

def main():
    contactos = []  # Lista para almacenar los contactos
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_contacto(contactos)
        elif opcion == '2':
            listar_contactos(contactos)
        elif opcion == '3':
            buscar_contacto(contactos)
        elif opcion == '4':
            eliminar_contacto(contactos)
        elif opcion == '5':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()

