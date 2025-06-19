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
    print("\n--- Agregar Contacto ---")
    nombre = input("Nombre: \n")
    telefono = input("Teléfono: \n")
    email = input("Email: \n")
    contacto = {"nombre": nombre, "telefono": telefono, "email": email}
    contactos.append(contacto)
    print("Contacto agregado exitosamente.")

def listar_contactos(contactos):
    print("\n--- Lista de Contactos ---")
    if not contactos:
        print("No hay contactos guardados.")
        return
    for i, contacto in (contactos):
        print(f"{i + 1}. Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
        
        
def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Agregar Contacto")
    print("2. Listar Contactos")
    print("3. Buscar Contacto")
    print("4. Eliminar Contacto")
    print("5. Salir")
    print("----------------------")
