import random
import math
import os

os.system("cls || clear")  # czyszczenine konsoli
list_of_temp = []  # lista elementów
i = 0  # temperatura szukana
n = 1000  # liczba elementów w liście

# losowanie wartości do listy
while i < n:
    # zakres temperatur (właściwie wartości bo zero bezwzgledne to -273)
    r = random.randrange(-50, 50)
    list_of_temp.append(r)
    i += 1
print(list_of_temp)

najmniejsza = None
najwieksza = None
najblizsza_zeru = None
for i in list_of_temp:

    if i == 0:
        print("gratulacje znalazłeś 0 !!!!!!!!!!!!!!!!!")
        break

    if najblizsza_zeru == None or 0 - abs(najblizsza_zeru) < 0 - abs(i):
        najblizsza_zeru = abs(i)

    if najmniejsza == None or najmniejsza > i:
        najmniejsza = i

    if najwieksza == None or najwieksza < i:
        najwieksza = i


print("PRZED ZNALEZIENIEM ZERA: najmniejsza liczba to:", najmniejsza)
print("PRZED ZNALEZIENIEM ZERA: największa liczba to:", najwieksza)
print("PRZED ZNALEZIENIEM ZERA: najmniej oddalona liczba od 0 jest w odległosci: ", najblizsza_zeru)
