def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def binomial(n, k):
    if n == 0 and k == 0:
        return 1
    else:
        return factorial(n)/(factorial(k)*factorial(n-k))
