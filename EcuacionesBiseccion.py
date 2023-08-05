import math
def f(x):
	return -5+math.exp(2*x-1)
def biseccion_Camara_Reque_Adrian_Rafael_Ing_Informatica(a,b,tol,maxi):
	i=1
	FA=f(a)
	p = a+(b-a)/2
	while i<=maxi:
		p = a+(b-a)/2
		FP = f(p)
		if (FP==0) or ((b-a)/2 <tol):
			return p
		i=i+1
		if FA*FP > 0:
			a=p
			FA=FP
		else:
			b=p
	return p

print(biseccion_Camara_Reque_Adrian_Rafael_Ing_Informatica(1,2,0.01,7))