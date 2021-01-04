 
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import sympy as sp
from sympy import *
import math 

def objFunction(x1,x2):
    return 100*((x2-(x1**2))**2)+(1-x1)**2
    # return x1-x2+2*x1**2+2*x1*x2+x2**2


def Plot3D(X,Y,Z):
    fig = plt.figure(2)
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
                       # Customize the z axis.
    # ax.set_zlim(-1.01, 1.01)
    # ax.zaxis.set_major_locator(LinearLocator(10))
    # ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # Add a color bar which maps values to colors.
    # fig.colorbar(surf, shrink=0.5, aspect=5)
    ax.scatter3D(-1.2, 1, objFunction(-1.2,1), c=objFunction(-1.2,1), cmap='Greens')


    fig = plt.figure(1)
    ax1 = plt.axes(projection='3d')
    ax1.contour3D(X, Y, Z, 50, cmap='binary')

    plt.show()

def Hessian(f,x1,x2):
    # H.subs({x1 :1/sqrt(3),x2:1/sqrt(3)}
    H=hessian(f ,(x1,x2))
    return lambdify((x1,x2), H, modules='numpy')

def Jacobian(f,x1,x2):
    # F.jacobian((x1, x2)).subs({x1 :1/sqrt(3),x2:1/sqrt(3)}
    f=sp.Matrix([f])
    J=f.jacobian((x1,x2))
    return lambdify((x1,x2), J, modules='numpy')


def OFLambda(s,xi):
    Lambda=Symbol('Lambda')
    xi=sp.Matrix(xi)
    s=sp.Matrix(s)
    Xi_1=xi+Lambda*s
    x1,x2=symbols('x1 x2')
    f=objFunction(Xi_1[0],Xi_1[1])

    
    
    

    return lambdify((Lambda), f, modules='numpy')

# s=np.array([[1],[1]])
# xi=np.array([[0],[0]])
s=[[4],[0]]
xi=[[-1],[1]]
OFF=OFLambda(s,xi)
# print(OFF(0.003846))





def GenerateQuadratic(t,x0,Lambda,s):
    ObjectiveFunction=OFLambda(s,x0)
    A = 0
    B = t
    C = 2 * t
    f_1 = ObjectiveFunction(A)
    f_2 = ObjectiveFunction(B)
    f_3 = ObjectiveFunction(C)

    f_A =  ObjectiveFunction(A)
    f_B = ObjectiveFunction(B)
    f_C = ObjectiveFunction(C)

    if (f_1 > f_A):
        f_C = f_1
        f_B = F(t / 2)
        Lambda_star = lambdastar(f_A, f_B, f_C, t / 2)
    elif (f_1 < f_A):
        f_C = f_1
        f_B = F(t / 2)
        Lambda_star = lambdastar(f_A, f_B, f_C, t / 2)
    a = f_A
    b = (4 * f_B - 3 * f_A - f_C) / 2 * t
    c = (f_C + f_A - 2 * f_B) / (2 * (t**2))

    Lambda_star = ((4 * f_B - 3 * f_A - f_C) /
                   (4 * f_B - 2 * f_C - 2 * f_A)) * t
    return f_A, f_B, f_C
