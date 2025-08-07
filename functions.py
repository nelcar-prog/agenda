def agregar_contacto(contactos):
    print("\n--- Agregar Contacto ---")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    contacto = {"nombre": nombre, "telefono": telefono, "email": email}
    contactos.append(contacto)
    print("Contacto agregado exitosamente.")


def listar_contactos(contactos):
    print("\n--- Lista de Contactos ---")
    if not contactos:
        print("No hay contactos guardados.")
        return
    for i, contacto in enumerate(contactos, start=1):
        print(
            f"{i}. Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}"
        )


def buscar_contacto(contactos):
    print("\n--- Buscar Contacto ---")
    if not contactos:
        print("No hay contactos para buscar.")
        return
    nombre_buscar = input("Ingrese el nombre del contacto a buscar: ").lower()
    encontrados = [c for c in contactos if nombre_buscar in c["nombre"].lower()]
    if encontrados:
        for contacto in encontrados:
            print(
                f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}"
            )
    else:
        print("No se encontró ningún contacto con ese nombre.")


def eliminar_contacto(contactos):
    print("\n--- Eliminar Contacto ---")
    if not contactos:
        print("No hay contactos para eliminar.")
        return
    nombre_eliminar = input("Ingrese el nombre del contacto a eliminar: ").lower()
    cantidad_inicial = len(contactos)
    contactos[:] = [c for c in contactos if nombre_eliminar not in c["nombre"].lower()]
    if len(contactos) < cantidad_inicial:
        print("Contacto(s) eliminado(s) exitosamente.")
    else:
        print("No se encontró ningún contacto con ese nombre para eliminar.")


def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Agregar Contacto")
    print("2. Listar Contactos")
    print("3. Buscar Contacto")
    print("4. Eliminar Contacto")
    print("5. Salir")
    print("----------------------")

