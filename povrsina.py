from math import sqrt
def IzracunajP(a,b,c):
    s=(a+b+c)/2
    P=sqrt(s*(s-a)*(s-b)*(s-c))
    return P
