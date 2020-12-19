from math import *
'''


h(Lambda)=a+b*Lambda+c*Lambda**2 ; c>0 to be minimum
Lambda=-b/(2*c)

We have the function value at X1, and lambda is zero, so we need to make use of this piece of info.
Then we'll generate two other quadratic equations:
A=0
B=T
C=2T
f=A+bA+xA^2
where T is up to the problem if there are quick flacuations T is small otherwise for a smooth gradually increasing function it could be large number.
'''

def F(x):
    # return (x1**2-x2)**2+(1-x1)**2
    # return x-8.5*x-31.0625*x-57*x +45
    return pow(x,5)-5*pow(x,3)-20*x+ 5


def lambdastar(f_A,f_B,f_C,t):
    return ((4 * f_B - 3 * f_A - f_C) / (4 * f_B - 2 * f_C - 2 * f_A)) * t


def GenerateQuadratic(t):
    A=0
    B=t
    C=2*t
    f_1=F(A)
    f_2=F(B)
    f_3=F(C)

    f_A=F(A)
    f_B=F(B)
    f_C=F(C)

    if (f_1>f_A):
        f_C=f_1
        f_B=F(t/2)
        Lambda_star=lambdastar(f_A,f_B,f_C,t/2)
    elif(f_1<f_A):
        f_C=f_1
        f_B=F(t/2)
        Lambda_star=lambdastar(f_A,f_B,f_C,t/2)
    a=f_A
    b=(4*f_B-3*f_A-f_C)/2*t
    c=(f_C+f_A-2*f_B)/(2*(t**2))

    Lambda_star=((4*f_B-3*f_A-f_C)/(4*f_B-2*f_C-2*f_A))*t
    return f_A,f_B,f_C

print(GenerateQuadratic(0.5))

