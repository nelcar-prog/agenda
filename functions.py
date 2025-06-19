def buscar_contacto(contactos):
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