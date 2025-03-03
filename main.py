# ZADANIE 6

plik = open("dane.txt")
dane = plik.read()
lista = dane.split("\n")
print(lista)


# a)
def pierwszaLiczbaRownaOstatniej(liczba):
    if liczba[0] == liczba[-1]:
        return True
    return False


# b)
def dziesietnyIOsemkowy(liczba):
    suma = 0
    mnoznik = 1
    dlugosc = len(liczba)
    for i in range(dlugosc - 1, -1, -1):
        suma = suma + int(liczba[i]) * mnoznik
        mnoznik = mnoznik * 8
    return suma


# iteracja rozwiązanie b)
odpowiedz = 0
for el in lista:
    if pierwszaLiczbaRownaOstatniej(str(dziesietnyIOsemkowy(el))):
        odpowiedz += 1
print(odpowiedz)


# c)
def mniejszaOdPoprzedzajacej(liczba):
    for i in range(len(liczba)-1):
        if liczba[i] > liczba[i + 1]:
            return False
        return True
print(mniejszaOdPoprzedzajacej("122455"))

odpowiedz2 = 0
for el in lista:
    if mniejszaOdPoprzedzajacej(el):
        odpowiedz2 += 1
print(odpowiedz2)
