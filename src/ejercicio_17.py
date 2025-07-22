numero = (input("Ingrese un numero positivo: "))
suma_digitos = 0
if numero.isdigit():
    suma_digitos = 0
    for i in numero:
        suma_digitos += int(i)
    print(f"La suma de los dígitos es {suma_digitos}")
else:
    print("Debe ingresar un número positivo")