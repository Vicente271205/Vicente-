
------------------ 
def saludo (nombre): #este da un saludo
    print(f"hola, {nombre}")

saludo ()

--------------

def suma(valor1, valor2):
    return valor1+valor2

resultado=suma(4,5)
print(resultado)

----------------

def multiplicacion(valor1, valor2):
    return valor1 * valor2

resultado=multiplicacion(10,3)

print(f"El area del triangulo es {resultado}")
##########
##########
base = float(input("Ingrese la base del triangulo"))
altura = float(input("Ingrese la altura del triangulo"))

def multiplicacion(base, altura):
    return base * altura

resultado=multiplicacion(base,altura)

print(f"El area del triangulo es {resultado}")

------------------

nombre = str(input("Ingrese su nombre"))
nota1 = float(input("Ingrese su primer nota"))
nota2 = float(input("Ingrese su segunda nota"))

def evaluar(nombre, nota1, nota2):
    promedio = (nota1+nota2)/2

    if promedio >= 6:
        return (f"{nombre} aprobó con {promedio}")
    else:
        return (f"{nombre} desaprobó con {promedio}")

resultado=evaluar(nombre,nota1,nota2)
print(resultado)

----------------

valor1 = float(input("Ingrese el primer valor"))
valor2 = float(input("Ingrese el segundo valor"))

if valor1 >0 and valor2 >0:
    print("Los 2 valores son positivos")
elif valor1 > 0 and valor2 == 0:
    print("El primer valor es positivo y el segundo es igual a 0")
elif valor1 >0 and valor2 <0:
    print ("El primer valor es positivo y el segundo es negativo")
elif valor1 and valor2 <0:
    print("Los 2 valores son negativos")
elif valor1 == 0 and valor2 == 0:
    print("Los 2 valores son iguales a 0")
elif valor1 ==0 and valor2 >0:
    print("El primer valor es igual a 0 y el segundo es positivo")
elif valor1 <0 and valor2 >0:
    print("El primer valor es negativo y el segundo es positivo")

------------------

 #GRILLA SORTEO#

import random

def generar_grilla():
    grilla = []
    for i in range(46):
        grilla.append(i)
    return grilla

def generar_jugador():
    return random.sample(range(46),6)

jugador1= generar_jugador
jugador2= generar_jugador

def sorteo_quini6(grilla, jugador1, jugador2):
    sorteo = []
    while grilla and jugador1 and jugador2:
        numero_sorteo = random.choice(grilla)
        sorteo.append(numero_sorteo)
        print(f"Numero sorteado: {numero_sorteo}")
        
        if numero_sorteo in jugador1:
            jugador1.remove(numero_sorteo)
            print("jugador1 tenia el numero")
        
        if numero_sorteo in jugador2:
            jugador2.remove(numero_sorteo)
            print("jugador2 tenia el numero")
        grilla.remove(numero_sorteo)
    return sorteo, jugador1, jugador2
    
def mostrar_resultados(sorteo,jugador1,jugador2):
    print("\n Numeros sorteados:", sorteo)
    print("jugador1 restantes:", jugador1)
    print("jugador2 restantes:", jugador2)
    
    if not jugador1 and not jugador2:
        print("Empate")
    elif not jugador1:
        print("jugador1 ganó")
    elif not jugador2:
        print("jugador2 ganó")

def main():
    
    grilla = generar_grilla()
    jugador1 = generar_jugador()
    jugador2 = generar_jugador()
    
    print("jugador1: ", jugador1)
    print("jugador2: ", jugador2)
    
    sorteo, restante1, restante2 = sorteo_quini6(grilla,jugador1,jugador2)
    mostrar_resultados(sorteo, restante1,restante2)

if __name__=="__main__":
    main()

--------------------

archivo= open("C:\Users\Labo\Desktop\consumo_bandwidth.log", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

#############

archivo = open ("C:\Users\Labo\Desktop\consumo_bandwidth.log", "w")
archivo.write("Hola chicos")
archivo.close()

