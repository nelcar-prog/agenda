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