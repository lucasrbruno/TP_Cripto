from curva import *
from EuclidianExtended import *

class Ponto:
	def __init__(self, x, y, infinito_bool):
		self.x = x
		self.y = y
		self.infinito_bool = infinito_bool

def pontonaCurva(ponto, curva):
	if(ponto.infinito_bool == True):
		return True
	if ((ponto.y * ponto.y) % curva.p) == ((ponto.x * ponto.x * ponto.x + curva.a * ponto.x + curva.b) % curva.p):
		return True
	return False	
			

def somaPontos(ponto1, ponto2, curva):
	
	
	p = curva.p	
	
	if ponto1.infinito_bool == True:
		print("RES = PONTO_2")
		return ponto2
	
	if ponto2.infinito_bool == True:
		print("RES = PONTO_1")
		return ponto1
	
	if ponto1.x % p  == ponto2.x % p and ponto1.y % p == -ponto2.y % p:
		p_inf = Ponto(None, None, True)
		return p_inf

				
	if ponto1.x != ponto2.x and ponto1.y != ponto2.y:
		m = ((ponto2.y - ponto1.y) * (euclidian(p, ponto2.x - ponto1.x))) % p

	else:
		m = ((3 * ponto1.x * ponto1.x + curva.a) * euclidian(p, ((2 * ponto1.y) % p))) % p	 
 
	r_x = (m * m - ponto1.x - ponto2.x) % p
	r_y = (m * (ponto1.x - r_x) - ponto1.y) % p
	print(str(ponto1.x), str(ponto1.y) + " + " + str(ponto2.x), str(ponto2.y) + " = " + str(r_x), str(r_y))
	resultado = Ponto(r_x,r_y, False)
	return resultado

def multiplicacaoPonto(ponto, curva, n):
	res = Ponto(None,None,True)  #ponto no infinito
	ponto_soma = ponto
	while n != 0:
		if n % 2 == 1:
			print("ADDING RES:")
			res = somaPontos(res, ponto_soma, curva)
		print("ADDING PONTO_SOMA:")
		ponto_soma = somaPontos(ponto_soma, ponto_soma, curva)
		n = n // 2 
	return res	
	
curva = CurvaEliptica(2,1, 5)
ponto = Ponto(0,1, False)
som = somaPontos(ponto, ponto, curva)
print(som.x, som.y)
mult = multiplicacaoPonto(ponto, curva, 10)
print(mult.x, mult.y)		

		
