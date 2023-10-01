def podobne(n,k,A,B):
    if A[0:k-1]==B[(n-k):n-1] and A[k:n-1]==B[0:n-k-1]:
        return True
    else:
        return False
def znajdz_podobne(n,A,B):
    for i in range(0,n-1):
        print(i)
        if podobne(n,i,A,B)==True:
            return True
    return False
A=[4, 2, 4, 4, 2, 6]
B=[4, 4, 2, 6, 4, 2]
print(podobne(6,2,A,B))
print(znajdz_podobne(6,A,B))