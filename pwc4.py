import random
import sys
import math

list_of_temp = [] # lista elementów
i = 0 # temperatura szukana 
n = 100 # liczba elementów w liście

#losowanie wartości do listy
while i < n:
    r = random.randrange(-300, 300) # zakres temperatur (właściwie wartości bo zero bezwzgledne to -273)
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
for i in lista:
    
    # przy każdej iteracji, sprawdzamy czy zmienna i 
    # jest mniejsza lub większa niż przechowywane przez
    # nas zmienne
    if i == 0:
        print("gratulacje znalazłeś 0 ")
        break
    
    if najmniejsza == None or najmniejsza > i: 
        najmniejsza = abs(i)
        
    if najwieksza == None or najwieksza < i:
        najwieksza = i
        
print ("najmniejsza liczba to:", najmniejsza)
print ("największa liczba to:", najwieksza)