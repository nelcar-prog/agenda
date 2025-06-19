def agregar_contacto(contactos):
    """
    Agrega un nuevo contacto a la lista.
    """
    print("\n--- Agregar Contacto ---")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    contacto = {"nombre": nombre, "telefono": telefono, "email": email}
    contactos.append(contacto)
    print("Contacto agregado exitosamente.")

def listar_contactos(contactos):
    """
    Lista todos los contactos.
    """
    print("\n--- Lista de Contactos ---")
    if not contactos:
        print("No hay contactos guardados.")
        return
    for i, contacto in enumerate(contactos):
        print(f"{i + 1}. Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")

def buscar_contacto(contactos):
    """
    Busca un contacto por nombre.
    """
    print("\n--- Buscar Contacto ---")
    if not contactos:
        print("No hay contactos para buscar.")
        return
    nombre_busqueda = input("Ingrese el nombre del contacto a buscar: ").lower()
    contactos_encontrados = [contacto for contacto in contactos if nombre_busqueda in contacto['nombre'].lower()]
    if contactos_encontrados:
        print("Contactos encontrados:")
        for contacto in contactos_encontrados:
            print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
    else:
        print("No se encontró ningún contacto con ese nombre.")

def eliminar_contacto(contactos):
    """
    Elimina un contacto por nombre.
    """
    print("\n--- Eliminar Contacto ---")
    if not contactos:
        print("No hay contactos para eliminar.")
        return
    nombre_eliminar = input("Ingrese el nombre del contacto a eliminar: ").lower()
    longitud_inicial = len(contactos)
    # Se crea una nueva lista excluyendo los contactos a eliminar
    contactos[:] = [contacto for contacto in contactos if nombre_eliminar not in contacto['nombre'].lower()]
    if len(contactos) < longitud_inicial:
        print("Contacto(s) eliminado(s) exitosamente.")
    else:
        print("No se encontró ningún contacto con ese nombre para eliminar.")

def mostrar_menu():
    """
    Muestra las opciones del menú principal.
    """
    print("\n--- Menú Principal ---")
    print("1. Agregar Contacto")
    print("2. Listar Contactos")
    print("3. Buscar Contacto")
    print("4. Eliminar Contacto")
    print("5. Salir")
    print("----------------------")