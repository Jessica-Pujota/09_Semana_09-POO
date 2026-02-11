class Producto:  #Clase que representa un producto en el inventario. Esta clase encapsula los atributos y comportamientos básicos de un producto.
    
    def __init__(self, id_producto: int, nombre: str, cantidad: int, precio: float):
        """
        Constructor de la clase Producto.  Este método se llama al crear una nueva instancia de Producto y se encarga de inicializar los atributos del producto con los valores proporcionados.
        :param id_producto: Un identificador único para el producto.
        """
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio
    
    # Getters y Setters para cada atributo
    # Estos métodos permiten un acceso controlado a los atributos de la clase
    
    @property
    def id(self) -> int:  #Obtiene el ID del producto
        return self._id
    
    @id.setter
    def id(self, nuevo_id: int):   #Establece un nuevo ID para el producto
        self._id = nuevo_id
    
    @property
    def nombre(self) -> str: # Obtiene el nombre del producto
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre: str): #Establece un nuevo nombre para el producto
        self._nombre = nuevo_nombre
    
    @property
    def cantidad(self) -> int:  #Obtiene la cantidad disponible del producto
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self, nueva_cantidad: int): #Establece una nueva cantidad para el producto
        if nueva_cantidad >= 0:
            self._cantidad = nueva_cantidad
        else:
            print("Error: La cantidad no puede ser negativa")
    
    @property
    def precio(self) -> float:  #Obtiene el precio del producto
        return self._precio
    
    @precio.setter
    def precio(self, nuevo_precio: float):  #Establece un nuevo precio para el producto
        if nuevo_precio >= 0:
            self._precio = nuevo_precio
        else:
            print("Error: El precio no puede ser negativo")
    
    def __str__(self) -> str:   #Este método especial se llama cuando se convierte el objeto a una cadena, por ejemplo, al imprimirlo. Proporciona una representación legible del producto, mostrando su ID, nombre, cantidad y precio de manera clara.
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"
    
    def to_dict(self) -> dict: # Convierte el producto a un diccionario. Útil para serialización o para mostrar datos de forma estructurada.        """
        return {
            'id': self._id,
            'nombre': self._nombre,
            'cantidad': self._cantidad,
            'precio': self._precio
        }