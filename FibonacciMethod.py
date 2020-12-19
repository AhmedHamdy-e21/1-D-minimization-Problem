#https://www.youtube.com/watch?v=GAafWFRGP7k&ab_channel=OscarVeliz
from math import *
def F(x1,x2):
    return 100*(x2-x1)**2+(1-x1)**2
def Fexample(x):
    return x**2

def Fibbonacci(n):
    fib=[]
    fib.append(1)
    fib.append(1)
    i = 2
    while n>fib[i-1]:
        fib.append(fib[i-1]+fib[i-2])
        i+=1

    return fib,i

def Fibbonaccibynumber(n):
    fib=[]
    fib.append(1)
    fib.append(1)
    for i in range(n):
        if (i>2 or i==2):
            fib.append(fib[i - 1] + fib[i - 2])
        else:
            continue
    return fib








def swap(xl,xu):
    return xu,xl


def FibMinimization(A1,B1, tolerance=None, N=None):
    if N!=None:
        N=N+1
        Sequence=Fibbonaccibynumber(N)
    elif tolerance!=None:
        LargerFib = (B1-A1) / tolerance
        Sequence,N = Fibbonacci(LargerFib)

    else:
        return False

    J=1
    xl=None
    xu=None
    L = (B1 - A1)
    L2star = (Sequence[N - J - 2] / Sequence[N - 1]) * L
    L = (B1 - A1)
    if L2star > (L / 2):
        xl = B1 - L2star
        xu = A1 + L2star
    else:
        xl = A1 + L2star
        xu = B1 - L2star
    while J<N-1:
        fl=Fexample(xl)
        fu=Fexample(xu)
        if (fl>fu):
            A1=xl
            L2star = (Sequence[N - J - 2] / Sequence[N - 1]) * L
            xl=A1+L2star
            fl = Fexample(xl)
            if xl > xu:
                xl,xu=swap(xl,xu)
                fl,fu=swap(fl,fu)

        elif(fl<fu):
            B1=xu
            L2star = (Sequence[N - J - 2] / Sequence[N - 1]) * L
            xu=B1-L2star
            fu = Fexample(xu)
            if xl > xu:
                xl, xu = swap(xl, xu)
                fl, fu = swap(fl, fu)
        J+=1


    return xl,xu,fl,fu

print(FibMinimization(-5,15,N=7))