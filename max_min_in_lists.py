# przykład rozwiązania zadania
lista = [1,3,7,11,2,-6,0]
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
    
    if najmniejsza == None or najmniejsza > i: 
        najmniejsza = i
        
    if najwieksza == None or najwieksza < i:
        najwieksza = i
        
print ("najmniejsza liczba to:", najmniejsza)
print ("największa liczba to:", najwieksza)