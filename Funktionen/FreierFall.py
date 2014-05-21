#!/usr/bin/env Python2

def fallHoehe(h_0, t, g = 9.81):
    return float(h_0)-float(g)*float(t)*float(t)/2.0

eingabeH_0 = raw_input("Starthoehe= ")
eingabeT = raw_input("Zeit= ")
eingabeBeschl = raw_input("Erdbeschleunigung= ")

h_t = fallHoehe(eingabeH_0, eingabeT, eingabeBeschl)
print "Hallhoehe zum Zeitpunkt"+str(eingabeT)+"= ",
print h_t

print "mit Keyword-Parametern: ",
print fallHoehe(t=eingabeT, g=eingabeBeschl, h_0=eingabeH_0)

print "ohne Eingabe der Erdbeschleunigung: ",
print fallHoehe(eingabeH_0, eingabeT)
