total = 0
while True:
    numero = input("Para salir  0 \n Ingrese el numero que quiere sumar: ")
    if numero == "0":
        break
    total +=  float(numero)
print(f"La suma total es {total}")