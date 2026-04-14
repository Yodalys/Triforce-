#tuplas
inventario = [
    (1, "Computadora", 800 ), #id, nombre, precio 
    (2, "Impresora", 150), #id, nombre, precio
    (3, "Silla", 120), #id, nombre, precio
    (4, "Escritorio", 300) #id, nombre, precio  
]
def mostrar_inventario(inventario):
    print("Inventario de productos:")
    for producto in inventario:
        id_producto, nombre_producto, precio_producto = producto
        print(f"ID: {id_producto}, Nombre: {nombre_producto}, Precio: ${precio_producto:<10.2f}")
mostrar_inventario(inventario)
