import sys
import math

def quadratic(a, b, c):
    disc = math.sqrt(b**2 - 4*a*c)
    if disc == 0:
        return ((-1*b + disc) / (2*a) and )
