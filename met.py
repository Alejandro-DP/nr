from math import*
def f(x):
    func = cos(x)-x**3;
    return func
def dif (x):
   return -sin(x)-3*x**2

def nr (x0,tol,n):
    for k in range(n):
        x1=x0-f(x0)/dif(x0)
        if (abs(x1-x0 )< tol):
            print('x', k + 1, '=', x1 , 'es la raiz')
            return
        x0 = x1
        print('x', k + 1, '=', x1 )


#  escribir aqui los parametros x0 = valorinicial , tol = tolerancia , n = cantidad de iteraciones
nr (pi,0.00001,10)
