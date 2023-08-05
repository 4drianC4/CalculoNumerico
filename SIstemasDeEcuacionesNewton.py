import numpy as np
def f(x,y):
	return 3*(x**2)-27*y
def g(x,y):
    return 3*(y**2)-27*x
def dfx(x,y):
	return 6*x
def dfy(x,y):
    return -27

def dgx(x,y):
    return -27
def dgy(x,y):
    return 6*y

def newton_sistemas_Camara_Reque_Adrian_Rafael_Ing_Informatica(a,b,maxi):
	i=0

	while (i<maxi):
		jacobi = np.array([[dfx(a, b), dfy(a, b)], [dgx(a, b), dgy(a, b)]])
		invert = np.linalg.inv(jacobi)
		mat1 = np.array([[a],[b]])
		mat3 = np.array([[f(a,b)],[g(a,b)]])
		p= mat1-np.dot(invert,mat3)
		i=i+1
		a=p.flat[0]
		b=p.flat[1]
	return p
tabla=newton_sistemas_Camara_Reque_Adrian_Rafael_Ing_Informatica(8,5,4)
tabla=np.array(tabla)
np.set_printoptions(precision=6)
print("Solución: ",end = '')
print(tabla)