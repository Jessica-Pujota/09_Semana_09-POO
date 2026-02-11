# Sistema de Gestión de Inventarios

Un sistema simple de gestión de inventarios para una tienda, implementado en Python utilizando Programación Orientada a Objetos.

## Características

- Gestión completa de productos (CRUD)
- Validación de entradas de usuario
- Búsqueda por nombre con coincidencias parciales
- Interfaz de consola interactiva
- Organización modular del código

### Estructura del Proyecto
##### inventario_tienda_app
- ##### modelos 
- ##### servicios
- ##### main.py

### Uso
El sistema presenta un menú interactivo con las siguientes opciones:

- Añadir producto: Permite agregar un nuevo producto al inventario
- Eliminar producto: Elimina un producto por su ID
- Actualizar producto: Modifica la cantidad o precio de un producto existente
- Buscar producto: Encuentra productos por nombre (coincidencias parciales)
Listar inventario: Muestra todos los productos en el inventario
- Valor total: Calcula el valor total del inventario
- Salir: Termina la ejecución del programa

El sistema está diseñado siguiendo los principios de la Programación Orientada a Objetos:

- Encapsulamiento: Los atributos de las clases son privados y se acceden mediante getters y setters
- Modularidad: El código está organizado en módulos separados por responsabilidades
- Reutilización: Las clases pueden ser extendidas y reutilizadas

### Ejemplos de Uso
El sistema incluye productos de ejemplo para facilitar las pruebas:

- Laptop HP - 10 unidades - $899.99
- Mouse inalámbrico - 50 unidades - $25.50
- Teclado mecánico - 20 unidades - $75.00
- Monitor 24" - 15 unidades - $199.99
- Audífonos Bluetooth - 30 unidades - $49.99