#Preguntar al usuario el articulo y su preccio y añaddir el par al diccionario, hasta que el usuario decida teeminar. Despues se debe mostrar por pantalla la lista de la compra y el coste total
#creamos un diccionario vacio para almacenar los articulos y sus precios
cesta = {}
while True:
    articulo = input("Ingrese el artículo (o 'terminar' para finalizar): ")
    if articulo.lower() == 'terminar':
        break
    precio = float(input(f"Ingrese el precio de {articulo}: "))
    cesta[articulo] = precio

# Mostrar la lista de la compra y el coste total
print("\nLista de la compra:")
total = 0
for articulo, precio in cesta.items():
    print(f"{articulo} | ${precio}")
    total += precio

print(f"\nCoste total: ${total}")
