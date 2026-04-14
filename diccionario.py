#creamos un diccioanrio de un coche
coche = {
    "marca": "Toyota", 
    "modelo": "Corolla",
    "año": 2020,
    "color": "Rojo",
    "precio": 20000
}

#1. Acceder a unn valor usando su clave
print (f"El coche es un {coche['marca']} {coche['modelo']} del año {coche['año']} y es de color {coche['color']} y cuesta ${coche['precio']}")
#2. Agregar o modificar un valor
coche["año"] = 2021  # Modificar el año
coche["transmision"] = "Automática"  # Agregar una nueva clave-valor