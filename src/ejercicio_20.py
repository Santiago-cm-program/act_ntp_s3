n = 0
a= 0
while True:
    n=int(input("Para salir ingrese el valor -1\n Ingrese las edades para determinar la mayor"))
    if n == -1:
        break
    if n > a:
        a = n
print(f"La edad mayor es {a}")
    