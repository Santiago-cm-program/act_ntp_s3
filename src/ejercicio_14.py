import random
while True:
    numero=int(input("Para el juego de la adivinanza, ingrese un numero del 1 al 10: "))
    n= random.randint(1,10)
    print(n)
    if n== numero:
        print(f"El numero correcto es {n}")
        break