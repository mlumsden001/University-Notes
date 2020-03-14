def product(A, k):
    count = 0
    n = len(A)
    x = 0

    for j in range(x,n):
        
        for i in range(x, j):
            if A[j]*A[i] <= k:
                count += 1
    

    return count

A = [1,1,3,5,6]
print(product(A, 5))