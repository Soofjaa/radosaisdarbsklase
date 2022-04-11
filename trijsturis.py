import math

def laukumstrissturis(a,b):
    return (a+b)/2
def laukumstrissturis1(a,b,c):
    pe = ((a+b+c)//2)
    return math.sqrt( (pe)*(pe-a)*(pe-b)*(pe-c) )

def perimetrstrissturis(a,b,c):
    return (a+b+c)
def augstumstrissturis(p,a):
    return ((2*p)-a)