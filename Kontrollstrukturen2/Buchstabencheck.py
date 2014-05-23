
def onlyENISRAT (stri) :
    s = set(stri.lower())
    s2 = set(["e","n","i","s","r","a","t","d","h","u"])

    s3 = s.intersection(s2)

    if s3:
        return True
    else :
        return False

def notInStr(stri):
    s = set(["e","n","i","s","r","a","t","d","h","u"])
    s2 = set(stri)
    return s2.difference(s)

eing = raw_input("Eingabe= ")
print onlyENISRAT(eing)
print notInStr(eing)
