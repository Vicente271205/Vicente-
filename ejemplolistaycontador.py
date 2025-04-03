
frutas = ["Manzana", "Pera", "Uva", "Mandarina"]

#print(frutas[1]) #hace que aparezca solo el item 1, la pera

frutas.append("Banana") #Agrega banana a la lista

frutas.insert(2, "Durazno") #inserta durazno en el lugar del item 2, la uva 

#frutas.remove("Uva") #remueve uva de la lista

#frutas.sort() #ordena el item en la lista

#frutas.reverse() #invierte el orden de los items de la lista

for fruta in frutas:
    print(fruta)

'''
numeros = ["1", "2", "3", "4"]
for numero in numeros:
    print (numero)
'''

#while // repite un bloque mientras una condicion sea verdadera
# contador = 3 // asigno un valor a la variable
# contador == 3 // hago una comparacion

'''
contador = 0

while contador <= 5:
    print(contador)
    contador +=1

contador = 0
while True:
    print(contador)
    contador +=1
    if contador == 5:
        break
'''