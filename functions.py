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