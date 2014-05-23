file1 = open("newFile", "w")
with open ("testdata",) as f:
    i=1
    for line in f:
        file1.write(str(i)+ " "  + line)
        i+=1
