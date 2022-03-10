import sys as system
import math

system.stdout.write("wpisz dowolną liczbę: ")
liczba1 = system.stdin.readline()
system.stdout.write("wpisz dowolną liczbę: ")
liczba2 = system.stdin.readline()
system.stdout.write("wpisz dowolną liczbę: ")
liczba3 = system.stdin.readline()

wynik = math.pow(int(liczba1),int(liczba2)) + int(liczba3)

print(wynik)