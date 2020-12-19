from math import *
def swap(xl,xu):
    return xu,xl
def Fexample(x):
    return 0.65-(0.75/(1+x**2))-0.65*x*atan(1/x)
    # return 2*sin(x)-((x**2)/10)

def swaplarger(xl,xu,fl,fu):

    if xl > xu:
        xl, xu = swap(xl, xu)
        fl, fu = swap(fl, fu)
    return xl,xu,fl,fu

def GoldenSection(A1,B1,N):
    J=1
    xl=A1
    xu=B1
    d = 0.618 * (B1 - A1)
    xl=xl+d
    xu=xu-d
    fl = Fexample(xl)
    fu = Fexample(xu)
    #
    xl, xu, fl, fu = swaplarger(xl, xu, fl, fu)
    while J<N:
        print(xl, xu, fl, fu)
        if (fl > fu):
            A1 = xl
            d=0.618*(B1-A1)
            xl = A1 + d
            fl = Fexample(xl)
            xl, xu, fl, fu = swaplarger(xl, xu, fl, fu)

        elif (fl < fu):
            B1 = xu
            d=0.618*(B1-A1)
            # print(d,B1,A1)
            xu = B1 - d
            fu = Fexample(xu)
            xl, xu, fl, fu = swaplarger(xl, xu, fl, fu)
        J+=1

    print(xl, xu, fl, fu)

GoldenSection(0,3,14)
