print("Bienvenido a la pizzería Bella Napoli ")
Ve = input("¿Quieres una pizza vegetariana? (si/no): ").lower()
 
if Ve == "si":
    print("\nIngredientes vegetarianos disponibles:")
    print("1. Pimiento")
    print("2. Tofu")
   
    opcion = input("Elige un ingrediente (1 o 2): ")
   
    if opcion == "1":
        ingrediente = "Pimiento"
    elif opcion == "2":
        ingrediente = "Tofu"
    else:
        ingrediente = "Ingrediente no válido"
   
    print("\nTu pizza es vegetariana.")
   
elif Ve == "no":
    print("\nIngredientes no vegetarianos disponibles:")
    print("1. Pepperoni")
    print("2. Jamón")
    print("3. Salmón")
   
    opcion = input("Elige un ingrediente (1, 2 o 3): ")
   
    if opcion == "1":
        ingrediente = "Pepperoni"
    elif opcion == "2":
        ingrediente = "Jamón"
    elif opcion == "3":
        ingrediente = "Salmón"
    else:
        ingrediente = "Ingrediente no válido"
   
    print("\nTu pizza no es vegetariana.")
 
else:
    print("Opción no válida.")
    ingrediente = "Ninguno"
 
print("\nIngredientes de la pizza:")
print("- Mozzarella")
print("- Tomate")
print(f"- {ingrediente}")