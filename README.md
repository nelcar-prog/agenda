# Agenda

Aplicación de consola para administrar contactos. Permite agregar, listar, buscar y eliminar contactos.

## Requisitos

- Python 3.x instalado en el sistema.

## Instalación

1. Clona este repositorio:
    ```bash
    git clone <repo-url>
    cd agenda
    ```
2. (Opcional) Crea un entorno virtual y actívalo:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

## Uso

1. Ejecuta la aplicación:
    ```bash
    python main.py
    ```
2. Se mostrará el menú principal:

    ```
    --- Menú Principal ---
    1. Agregar Contacto
    2. Listar Contactos
    3. Buscar Contacto
    4. Eliminar Contacto
    5. Salir
    ----------------------
    ```

3. Selecciona una opción ingresando el número correspondiente:

   - **1. Agregar Contacto**: Ingresa nombre, teléfono y correo del nuevo contacto.
   - **2. Listar Contactos**: Muestra todos los contactos guardados.
   - **3. Buscar Contacto**: Escribe el nombre (o parte del nombre) para buscar coincidencias.
   - **4. Eliminar Contacto**: Escribe el nombre para eliminar los contactos que coincidan.
   - **5. Salir**: Termina la ejecución del programa.

Los contactos se mantienen solo en memoria durante la ejecución; al cerrar el programa se perderán.

## Contribuir

Las contribuciones son bienvenidas. Puedes abrir issues o enviar pull requests con mejoras.

