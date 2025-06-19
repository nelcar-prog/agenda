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
