from Utilities import *

# def GradfCubic(f,x1,x2):
#     # F.jacobian((x1, x2)).subs({x1 :1/sqrt(3),x2:1/sqrt(3)}
#     f=sp.Matrix([f])
#     J=f.jacobian((x1,x2))
    
#     return lambdify((x1,x2), J, modules='numpy')

def OFLambda(s,xi):
    Lambda=Symbol('Lambda')
    xi=sp.Matrix(xi)
    s=sp.Matrix(s)
    Xi_1=xi+Lambda*s
    x1,x2=symbols('x1 x2')
    f=objFunction(Xi_1[0],Xi_1[1])
    return lambdify((Lambda), f, modules='numpy')
    

def Gradient(s,xi):
    Lambda=Symbol('Lambda')
   

    xi=sp.Matrix(xi)
    s=sp.Matrix(s)
    Xi_1=xi+Lambda*s
    x1,x2=symbols('x1 x2')
    f=objFunction(Xi_1[0],Xi_1[1])
    f=sp.Matrix([f])
    Lambda=sp.Matrix([Lambda])
    J=f.jacobian(Lambda)

    return lambdify((Lambda), J, modules='numpy')
    # return J


def ObjFunctionGradient(Lambda,s,xi):
    # s=np.asarray(s).reshape(2,1)
    # s=s/np.linalg.norm(s,ord=1)
    gradf=Gradient(s,xi)
    s=np.asarray(s).reshape(2,1)
    s=s/np.linalg.norm(s,ord=1)
    gradient=s.T*gradf(Lambda)
    return gradient
    # return gradf(Lambda)

def generateCubic(s,xi,t):
    OF=OFLambda(s,xi)
    gradOF=Gradient(s,xi)

    A=0
    B=t
    f_A=OF(A)

    f_Aprime=gradOF(A)
    f_B=OF(t)

    f_Bprime=gradOF(t)
    Z=((3*(f_A-f_B))/B)+f_Aprime+f_Bprime
    Q=np.sqrt(Z**2-f_Aprime*f_Bprime)
    a=f_A
    b=f_Aprime
    c=-(1/B)*(Z+f_Aprime)
    d=(1/(3*(B**2)))*(2*Z+f_Aprime+f_Bprime)
    Lambdas1=B*((f_Aprime+Z-Q)/(f_Aprime+f_Bprime+2*Z))
    Lambdas2=B*((f_Aprime+Z+Q)/(f_Aprime+f_Bprime+2*Z))
    return a,b,c,d,f_A,f_Aprime,f_B,f_Bprime,Lambdas1,Lambdas2,OF(Lambdas1),OF(Lambdas2),gradOF(Lambdas2)



#s=[[4],[0]]
#xi=[[-1],[1]]
#t=0.01
#OFF=Gradient(s,xi)
#print(ObjFunctionGradient(0.001307223,s,xi))

#print(OFF(0.001307223))

#print(generateCubic(s,xi,t))

########################################################################################################################################################################
# The algorithm
########################################################################################################################################################################
# Firstly, normalize the direction

# Function to normalize right here
s=[[4],[3]] 
s=np.asarray(s).reshape(2,1)
s=s/np.linalg.norm(s,ord=2)

print(s)