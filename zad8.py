lista = [0]*2
a=0
wynik=0
while a < 2:
    lista[a] = int(input("Podaj liczbę"))
    a+=1
for b in lista:
    if(b%2==0):
        wynik = wynik+b

print("Odpowiedź: "+str(wynik))