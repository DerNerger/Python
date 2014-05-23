#!/usr/bin/env python2

x=0
with open("testdata") as item:
    for line in item:
        x += line.count("spam")

print x
