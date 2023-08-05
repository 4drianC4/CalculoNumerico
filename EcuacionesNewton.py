import math
def f(x):
	return -3+math.exp(x)+x**3
def df(x):
	return math.exp(x)+3*x**2

def newton_Camara_Reque_Adrian_Rafael_Ing_Informatica(a,tol,maxi):
	i=1
	while (i<maxi):
		p=a-f(a)/df(a)
		if abs(p-a)<tol:
			return p
		i=i+1
		a=p
	return p
print("Con el primer programa: ",end = '')
print(newton_Camara_Reque_Adrian_Rafael_Ing_Informatica(2,0.01,10))