import numpy as np

def I(n):
    temp = np.zeros((n,n))
    for i in range(n):
        temp[i][i] = 1
    return temp

def add(A, B):
    if A.shape == B.shape:
        for i in range(A.shape[0]):
            for j in range(A.shape[1]):
                A[i][j] = A[i][j]+B[i][j]
        return A
    else:
        print("can't add these arrays.")
        return False

def scalarmult(A, b):
    for i in range(A.shape[0]):
            for j in range(A.shape[1]):
                A[i][j] = A[i][j]*b
    return A

def matmult(A,B):
    if B.shape[0] != A.shape[1]:
        print("can't multiply these arrays.")
        return False
    else:
        C = np.zeros((A.shape[0],B.shape[1]))
        for j in range(B.shape[1]):
            for k in range(A.shape[0]):
                for i in range(B.shape[0]):
                    C[k][j] = C[k][j]+B[i][j]*A[k][i]
        return C

#testing for gabe

A = I(3)
B = I(5)
C = add(A, B)
D = add(A, A)
print(D)
print(matmult((I(3)+I(3)),np.array([[1,2,3],[4,5,6],[7,8,9]])))
print(np.array([[1,2,3],[4,5,6],[7,8,9]]))
print(scalarmult(np.array([[1,2,3],[4,5,6],[7,8,9]]),3))
