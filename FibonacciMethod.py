#https://www.youtube.com/watch?v=GAafWFRGP7k&ab_channel=OscarVeliz
from math import *
def F(x1,x2):
    return 100*(x2-x1)**2+(1-x1)**2
def Fexample(x):
    return 0.65-(0.75/(1+x**2))-0.65*x*atan(1/x)

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
    xl=0
    xu=0
    L = (B1 - A1)
    L2star = (Sequence[N - J - 2] / Sequence[N - 1]) * L
    print(Sequence)

    A=A1
    B=B1
    L = (B1 - A1)
    if L2star > (L / 2):
        xl = B1 - L2star
        xu = A1 + L2star
    else:
        xl = A1 + L2star
        xu = B1 - L2star

    while J<N-1:
        J += 1
        L = (B1 - A1)
        if L2star>(L/2):
            xl=B1-L2star
            xu=A1+L2star
        else:
            xl=A1+L2star
            xu=B1-L2star
        print(xu,xl)
        fl=Fexample(xl)
        fu=Fexample(xu)
        # print(fu,fl)
        if (fl>fu):
            A1=xl
            L2star = (Sequence[N - J - 2] / Sequence[N - 1]) * L
            # xl=A + L2star
            # xl=xu-xl
            # L2star = (Sequence[N - J - 2] / Sequence[N - 1]) * L
        elif(fu>fl):
            B1=xu
            L2star = (Sequence[N - J - 2] / Sequence[N - 1]) * L
            # print("Herer\n",(Sequence[N - J - 2] , Sequence[N - 1]))
            # xu = B - L2star
            # L2star=(Sequence[N-J-2]/Sequence[N-1])*L
        else:
            A1=xl
            B1=xu
            L2star=(Sequence[N-J-2]/Sequence[N-1])*(B1-A1)
            J += 1

        # print((Sequence[N-J-2],Sequence[N-J]),Sequence[N-J-3],Sequence[N-J])
        # print(xu,xl)
        # print(fl,fu)
    return xl,xu





#  Frame work:
#  First is to initialize and generate the fibonacci sequenc
# then

FibMinimization(0,3,N=6)