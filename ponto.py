from curva import *
from EuclidianExtended import *

class Ponto:
	def __init__(self, x, y, infinito_bool):
		self.x = x
		self.y = y
		self.infinito_bool = infinito_bool

def pontonaCurva(ponto, curva):
	if ((ponto.y * ponto.y) % curva.p) == ((ponto.x * ponto.x * ponto.x + curva.a * ponto.x + curva.b) % curva.p):
		return True
	return False	
			

def somaPontos(ponto1, ponto2, curva):
	if pontonaCurva(ponto1, curva) == False or pontonaCurva(ponto2,curva) == False:
		print("ERRO: ponto fora da curva.")
		return
	
	p = curva.p	
	
	if ponto1.infinito_bool == True:
		return ponto2
	
	if ponto2.infinito_bool == True:
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
	resultado = Ponto(r_x,r_y, False)
	return resultado

def multiplicacaoPonto(ponto, curva, n):
	res = ponto
	for i in range(n - 1):
		res = somaPontos(ponto, res, curva)
	return res