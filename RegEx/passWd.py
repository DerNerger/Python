import re
with open("/etc/passwd") as f:
    for line in f:
        lis = line.split(":")
        print lis[0]
        print lis[4]

