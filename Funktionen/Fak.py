#!usr/bin/env Python 2

def fak(zahl): 
    ergebnis = 1 
    for i in range(2, zahl+1): 
        ergebnis *= i
    return ergebnis

eingabe = int(raw_input("Eingabe= "))
print fak(eingabe)
