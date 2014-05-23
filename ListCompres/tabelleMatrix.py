def create_matrix (n,m):
    return [[0 for i in range(m)] for j in range(n)]

def row(a,b):
    return a[b]

def column(a,b):
    return [a[i][b] for i in range(len(a))]

def createImatrix(n):
    a =  [[0 for i in range(n)] for j in range(n)]
    for i  in range (n):
        a[i][i]=1
    return a

a = create_matrix(3,5)
print a

print row(a,0)
print column(a,1)
print createImatrix(3)
