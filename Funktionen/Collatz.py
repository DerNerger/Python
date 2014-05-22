#!/usr/bin/env python2 

def collatz_folge(n):
    n=int(n)
    liste.append(n)
    if n == 1:
        return
    if n % 2 == 0 :
        collatz_folge(n/2)
    else:
        collatz_folge(3*n+1)

liste = []

eingabe = raw_input("a_0= ")

collatz_folge(eingabe)
print liste
