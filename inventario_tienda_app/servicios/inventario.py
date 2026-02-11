from modelos.producto import Producto
class Inventario:  # Clase que gestiona el inventario de productos. Implementa las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) utilizando una lista como estructura de almacenamiento principal.
    
    def __init__(self): # Constructor de la clase Inventario. Inicializa una lista vacía para almacenar los productos.        """
        self._productos = []  # Lista privada para almacenar productos
    
    @property
    def productos(self) -> list:  #Obtiene la lista de productos (solo lectura)
        return self._productos.copy()
    
    def añadir_producto(self, producto: Producto) -> bool:  #Añade un nuevo producto al inventario.
        # Validar que el ID no esté repetido
        if self._buscar_por_id(producto.id) is not None:
            print(f"Error: Ya existe un producto con ID {producto.id}")
            return False
        self._productos.append(producto)
        print(f"Producto '{producto.nombre}' añadido correctamente.")
        return True
    
    def eliminar_producto(self, id_producto: int) -> bool:  #Elimina un producto del inventario por su ID.
        producto = self._buscar_por_id(id_producto)
        if producto is None:
            print(f"Error: No se encontró un producto con ID {id_producto}")
            return False
        self._productos.remove(producto)
        print(f"Producto con ID {id_producto} eliminado correctamente.")
        return True
    
    def actualizar_producto(self, id_producto: int, cantidad: int = None, precio: float = None) -> bool:  #Actualiza la cantidad o precio de un producto
        producto = self._buscar_por_id(id_producto)
        if producto is None:
            print(f"Error: No se encontró un producto con ID {id_producto}")
            return False
        
        # Actualizar solo los campos proporcionados
        if cantidad is not None:
            producto.cantidad = cantidad
        if precio is not None:
            producto.precio = precio
        print(f"Producto con ID {id_producto} actualizado correctamente.")
        return True
    
    def buscar_por_nombre(self, nombre_busqueda: str) -> list: # Busca productos por nombre, permitiendo coincidencias parciales.  
        if not nombre_busqueda:
            return []
        
        # Búsqueda insensible a mayúsculas/minúsculas
        nombre_busqueda = nombre_busqueda.lower()
        resultados = []
        
        for producto in self._productos:
            if nombre_busqueda in producto.nombre.lower():
                resultados.append(producto)
        return resultados
    
    def mostrar_todos(self) -> None: # Muestra todos los productos registrados en el inventario.
        """ Si el inventario está vacío, muestra un mensaje apropiado. De lo contrario, muestra una lista detallada de todos los productos, incluyendo su ID, nombre, cantidad y precio. Al final, muestra el total de productos registrados. """
       
        if not self._productos:
            print("El inventario está vacío.")
            return
        print("\n" + "="*60)
        print("INVENTARIO COMPLETO")
        print("="*60)
        
        for producto in self._productos:
            print(f"- {producto}")
        print("="*60)
        print(f"Total de productos: {len(self._productos)}")
        print("="*60)
    
    def _buscar_por_id(self, id_producto: int) -> Producto:  #Método privado para buscar un producto por su ID.
        for producto in self._productos:
            if producto.id == id_producto:
                return producto
        return None
    
    def obtener_producto_por_id(self, id_producto: int) -> Producto:   #Método público para obtener un producto por su ID.
        return self._buscar_por_id(id_producto)
    
    def calcular_valor_total_inventario(self) -> float: #Calcula el valor total del inventario.
        """Returns: float: Valor total del inventario (suma de cantidad * precio de todos los productos)"""
        total = 0.0
        for producto in self._productos:
            total += producto.cantidad * producto.precio
        return total