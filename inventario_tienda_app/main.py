from servicios.inventario import Inventario
from modelos.producto import Producto

def mostrar_menu(): #Muestra el menú principal del sistema.
    print("\n" + "="*50)
    print("SISTEMA DE GESTIÓN DE INVENTARIOS")
    print("="*50)
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Listar todos los productos")
    print("6. Ver valor total del inventario")
    print("7. Salir")
    print("="*50)

def obtener_entero(mensaje: str) -> int: #Solicita y valida la entrada de un número entero.
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: Por favor ingrese un número entero válido.")

def obtener_float(mensaje: str) -> float: #Solicita y valida la entrada de un número decimal.
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Error: El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("Error: Por favor ingrese un número decimal válido.")

def añadir_producto_interactivo(inventario: Inventario): # Interfaz interactiva para añadir un nuevo producto.
    print("\n--- AÑADIR NUEVO PRODUCTO ---")
    id_producto = obtener_entero("Ingrese el ID del producto: ")

    # Verificar si el ID ya existe
    if inventario.obtener_producto_por_id(id_producto) is not None:
        print(f"Error: Ya existe un producto con ID {id_producto}")
        return
    nombre = input("Ingrese el nombre del producto: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return
    cantidad = obtener_entero("Ingrese la cantidad: ")
    if cantidad < 0:
        print("Error: La cantidad no puede ser negativa.")
        return
    precio = obtener_float("Ingrese el precio unitario: ")
    
    # Crear y añadir el producto
    nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
    inventario.añadir_producto(nuevo_producto)

def eliminar_producto_interactivo(inventario: Inventario): #Interfaz interactiva para eliminar un producto.
    print("\n--- ELIMINAR PRODUCTO ---")
    
    if not inventario.productos:
        print("El inventario está vacío. No hay productos para eliminar.")
        return
    id_producto = obtener_entero("Ingrese el ID del producto a eliminar: ")
    
    # Mostrar información del producto antes de eliminar
    producto = inventario.obtener_producto_por_id(id_producto)
    if producto:
        print(f"Producto encontrado: {producto}")
        confirmacion = input("¿Está seguro de que desea eliminar este producto? (s/n): ").lower()
        if confirmacion == 's':
            inventario.eliminar_producto(id_producto)
        else:
            print("Operación cancelada.")
    else:
        print(f"No se encontró un producto con ID {id_producto}")

def actualizar_producto_interactivo(inventario: Inventario): #Interfaz interactiva para actualizar un producto.
    print("\n--- ACTUALIZAR PRODUCTO ---")
    
    if not inventario.productos:
        print("El inventario está vacío. No hay productos para actualizar.")
        return
    id_producto = obtener_entero("Ingrese el ID del producto a actualizar: ")
    # Verificar si el producto existe
    producto = inventario.obtener_producto_por_id(id_producto)
    if producto is None:
        print(f"No se encontró un producto con ID {id_producto}")
        return
    print(f"\nProducto actual: {producto}")
    print("\n¿Qué desea actualizar?")
    print("1. Cantidad")
    print("2. Precio")
    print("3. Ambos")
    opcion = obtener_entero("Seleccione una opción (1-3): ")
    
    cantidad = None
    precio = None
    
    if opcion == 1 or opcion == 3:
        cantidad = obtener_entero("Ingrese la nueva cantidad: ")
        if cantidad < 0:
            print("Error: La cantidad no puede ser negativa.")
            return
    
    if opcion == 2 or opcion == 3:
        precio = obtener_float("Ingrese el nuevo precio: ")
    
    inventario.actualizar_producto(id_producto, cantidad, precio)

def buscar_producto_interactivo(inventario: Inventario): #Interfaz interactiva para buscar productos por nombre.
    print("\n--- BUSCAR PRODUCTO POR NOMBRE ---")
    
    if not inventario.productos:
        print("El inventario está vacío. No hay productos para buscar.")
        return
    
    nombre_busqueda = input("Ingrese el nombre o parte del nombre a buscar: ").strip()
    if not nombre_busqueda:
        print("Error: Debe ingresar un término de búsqueda.")
        return
    resultados = inventario.buscar_por_nombre(nombre_busqueda)
    
    if resultados:
        print(f"\nSe encontraron {len(resultados)} producto(s):")
        print("-" * 50)
        for producto in resultados:
            print(f"- {producto}")
        print("-" * 50)
    else:
        print(f"No se encontraron productos con el nombre '{nombre_busqueda}'")

def main(): # Función principal del programa. Controla el flujo del menú y las operaciones del sistema.
    # Crear instancia del inventario
    inventario = Inventario()
    
    # Agregar algunos productos de ejemplo
    productos_ejemplo = [
        Producto(1, "Laptop HP", 10, 899.99),
        Producto(2, "Mouse inalámbrico", 50, 25.50),
        Producto(3, "Teclado mecánico", 20, 75.00),
        Producto(4, "Monitor 24 pulgadas", 15, 199.99),
        Producto(5, "Audífonos Bluetooth", 30, 49.99)
    ]
    for producto in productos_ejemplo:
        inventario.añadir_producto(producto)
    
    print("¡Bienvenido al Sistema de Gestión de Inventarios!")
    print("Se han cargado algunos productos de ejemplo para comenzar.")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = obtener_entero("\nSeleccione una opción (1-7): ")
            if opcion == 1:
                añadir_producto_interactivo(inventario)
            elif opcion == 2:
                eliminar_producto_interactivo(inventario)
            elif opcion == 3:
                actualizar_producto_interactivo(inventario)
            elif opcion == 4:
                buscar_producto_interactivo(inventario)
            elif opcion == 5:
                inventario.mostrar_todos()
            elif opcion == 6:
                valor_total = inventario.calcular_valor_total_inventario()
                print(f"\nValor total del inventario: ${valor_total:.2f}")
            elif opcion == 7:
                print("\n¡Gracias por usar el Sistema de Gestión de Inventarios!")
                print("Saliendo del programa...")
                break
            else:
                print("Error: Opción no válida. Por favor seleccione una opción entre 1 y 7.")
        except KeyboardInterrupt:
            print("\n\nOperación interrumpida por el usuario.")
            break
        except Exception as e:
            print(f"\nError inesperado: {e}")
# Punto de entrada del programa
if __name__ == "__main__":
    main()