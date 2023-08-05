
import numpy as np
import math

def h(x,y):
    return (x**2+y**2+8)/10
def p(x,y):
    return (-x*y**2-x-8)/10
def hdx(x,y):
    return x/5
def hdy(x,y):
    return y/5
def pdx(x,y):
    return -(y**2-1)/10
def pdy(x,y):
    return -1*(x*y/5)
def puntoFijo_sistemas_Camara_Reque_Adrian_Rafael_Ing_Informatica(a,b,max):
    i = 0;
    res= np.array([])
    if (hdx(a,b)<1) and (hdy(a,b)<1) and (pdx(a,b)<1) and (pdy(a,b)<1):
        while (i < max):
            x = h(a,b)
            y = p(a,b)
            i=i+1
            a = x
            b = y
    else:
        res = np.array("valor erroneo")
    res = np.array([a,b])
    return res
np.set_printoptions(precision=6)
print(puntoFijo_sistemas_Camara_Reque_Adrian_Rafael_Ing_Informatica(0.5,0.2,6))