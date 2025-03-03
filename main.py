# ZADANIE 6

plik = open("dane.txt")
dane = plik.read()
lista = dane.split("\n")
print(lista)

# a)
def pierwszaLiczbaRównaOstatniej(liczba):
    if liczba[0] == liczba[-1]:
        return True
    return False

# b)
def dziesietnyIÓsemkowy(liczba):
    suma = 0
    mnoznik = 1
    dlugosc = len(liczba)
    for i in range(dlugosc-1, -1, -1):
        suma = suma + int(liczba[i]) * mnoznik
        mnoznik = mnoznik * 8
    return suma

# iteracja rozwiązanie b)
odpowiedz = 0
for el in lista:
    if pierwszaLiczbaRównaOstatniej(str(dziesietnyIÓsemkowy(el))):
        odpowiedz += 1
print(odpowiedz)

# c)
