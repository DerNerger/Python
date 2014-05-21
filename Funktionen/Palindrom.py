#!/usr/bin/env Python 2

def isPalindrom(wort):
    return wort == wort[::-1]

eingabe = raw_input("Eingabe= ")

print "isPalindrom= ",
print isPalindrom(eingabe)

print "isPalindrom Liste1= ",
print isPalindrom([1,3,5,7,2,5])

print "isPalindrom Liste2= ",
print isPalindrom([1,2,3,4,5,4,3,2,1])
