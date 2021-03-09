import random
import sys
import math
import os

os.system("cls || clear")


list_of_temp = [] # lista elementów
i = 0 # temperatura szukana 
n = 1000 # liczba elementów w liście

#losowanie wartości do listy
while i < n:
    r = random.randrange(-50, 50) # zakres temperatur (właściwie wartości bo zero bezwzgledne to -273)
    list_of_temp.append(r)
    i+=1
print(list_of_temp)


# przykład rozwiązania zadania
lista = list_of_temp #[1,3,7,11,2,-6,0]
# zmienne przecowujące najmniejsza i największa wartość
# na poczatku przypisujemy im wartość None, aby w pętli for
# wiedzieć że jest to pierwsza interakcja
# później zmienne, zaczynają zawierać liczby z listy
najmniejsza = None
najwieksza = None
najblizsza_zeru = None
for i in lista:
    
    # przy każdej iteracji, sprawdzamy czy zmienna i 
    # jest mniejsza lub większa niż przechowywane przez
    # nas zmienne
    if i == 0:
        print("gratulacje znalazłeś 0 !!!!!!!!!!!!!!!!!")
        break

    if najblizsza_zeru == None or  0 - abs(najblizsza_zeru) < 0 - abs(i):
        najblizsza_zeru = abs(i)

    if najmniejsza == None or najmniejsza > i: 
        najmniejsza = i
        
    if najwieksza == None or najwieksza < i:
        najwieksza = i

     
print ("PRZE ZNALEZIENIEM ZERA:  najmniejsza liczba to:", najmniejsza)
print ("PRZE ZNALEZIENIEM ZERA: największa liczba to:", najwieksza)
print("PRZE ZNALEZIENIEM ZERA: najmniej oddalona liczba od 0 jest w odległosci: ", najblizsza_zeru)