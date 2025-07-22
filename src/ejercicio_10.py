list_words = []
total_words=0
while True:
    word = input("Para salir y mostrar las palabras ingresadas utilizar la palabra 'Fin'\n Ingrese palabras:").lower()
    if word == "fin":
        break
    list_words.append(word)   
    
print(f"La Cantidad de palabras ingresadas fue {len(list_words)}")