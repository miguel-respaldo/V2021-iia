# indice: 0  1  2  3  4
lista1 = [1, 2, 4, 6, 19]
lista2 = [1, 2.4, "hola", 6.7, "bu"]

print(lista1[2])
print(lista1[4])
print(lista2[2])
print(lista2[3])
print("tamaño lista 1",len(lista1))
print("tamaño lista 2", len(lista2))

for elemento in lista2:
    print(elemento)

for indice in range(len(lista1)):
    print(lista1[indice])
