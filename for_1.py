cant_pares = 0
cant_impares = 0 
lista_número = "numeros: "

for i in range (1, 6): 
    n = int(input("digite el numero " + str(i) + ":"))

    lista_número = lista_número + str(n) + ","

    m = n%2

    if (m == 0):
        cant_pares = cant_pares + 1
    else:
        cant_impares = cant_impares + 1 

print("el total de numeros pares es:" , cant_pares)
print("el total de numeros impares es:" , cant_impares)