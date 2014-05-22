#!/usr/bin/env python2

listee = []
for i in range(10):
    input = raw_input("number: ")
    if input=="ende":
        break
    if int(input) >= 0:
        listee.insert(i, int(input))
        if sum(listee) > 42:
            break
print sum(listee)
