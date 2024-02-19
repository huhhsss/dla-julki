a = input("podaj słowo: ")

lista= []

for letter in a:
    lista.append(letter)

b = 0

while b < len(lista):
    print(lista[b], end=" ")
    b= b+2
    if b >= len(lista):
        break



