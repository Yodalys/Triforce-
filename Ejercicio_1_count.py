#preguntar al usuario por una frase y una letra, luego contar cuantas veces aparece esa letra en la frase y mostrar el resultado 
frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")    
count = 0
for caracter in frase:
    if caracter == letra:
        count += 1
print(f"La letra '{letra}' aparece {count} veces en la frase.")


