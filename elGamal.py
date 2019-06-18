from math import log
from curva import *
from EuclidianExtended import *
from ponto import *
from random import randint
class Criptograma:
	def __init__(self, r, c1, c2):
		self.r = r
		self.c1 = c1
		self.c2 = c2

def elGamal_encr(mensagem1, mensagem2, curva, pontop, q):
	primo = curva.p
	if pontonaCurva(pontop, curva) == False:
		print("ERRO: P fora da curva")
		return
<<<<<<< HEAD
	while(True):	
		k = randint(2, primo)	#chave efemera
		r = multiplicacaoPonto(pontop, curva, k)
		s = multiplicacaoPonto(q, curva, k)
		if s.infinito_bool == False:
			print("S = " + str(s.x), str(s.y)  + "\n")
			c1 = (s.x * mensagem1) % primo
			c2 = (s.y * mensagem2) % primo
			c = Criptograma(r, c1, c2)
			if c1 != 0 and c2 != 0:
				print("\nC1 = " + str(c1) +"\nC2 = " + str(c2) + "\nR = " + str(r.x), str(r.y))
				break
=======
	k = randint(2, primo)	#chave efemera
	#k = 2
	r = multiplicacaoPonto(pontop, curva, k)
	s = multiplicacaoPonto(q, curva, k)
	print("S = " + str(s.x), str(s.y)  + "\n")
	c1 = (s.x * mensagem1) % primo
	c2 = (s.y * mensagem2) % primo
	c = Criptograma(r, c1, c2)
	print("\nC1 = " + str(c1) +"\nC2 = " + str(c2) + "\nR = " + str(r.x), str(r.y))
>>>>>>> 351cf8f128ab6a68ba8aff57bdaac8aa213f72e9
	return c 

def elGamal_decr(c, curva, secretkey):
	primo = curva.p
	t = multiplicacaoPonto(c.r, curva, secretkey)
	print("T = " + str(t.x), str(t.y) + "\n")	
	m1 = (c.c1 * euclidian(primo, t.x)) % primo
	m2 = (c.c2 * euclidian(primo, t.y)) % primo
	print("\nM1 = " + str(m1) +"\nM2 = " + str(m2))
	return 

<<<<<<< HEAD
#primo = 0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF
#a = 0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFC
#b = 0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B
#curva = CurvaEliptica(a, b, primo)
primo = 41
secretkey = randint(2, primo)
#publickey_1 = Ponto(0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296, 0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5, False)
#publickey_2 = multiplicacaoPonto(publickey_1, curva, secretkey)
curva = CurvaEliptica(29, 51, primo)
publickey_1 = Ponto(21,32,False)
publickey_2 = multiplicacaoPonto(publickey_1, curva, secretkey)
mensagem1 = 21
mensagem2 = 27
=======
primo = 0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF
a = 0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFC
b = 0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B
curva = CurvaEliptica(a, b, primo)
publickey_1 = Ponto(0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296, 0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5, False)
secretkey = randint(2, primo) 
publickey_2 = multiplicacaoPonto(publickey_1, curva, secretkey)
#primo = 5
#curva = CurvaEliptica(2, 1, 5)
#ponto = Ponto(0,1,False)
#chavea = 4
#q = multiplicacaoPonto(ponto, curva, chavea)
mensagem1 = 15453
mensagem2 = 36325
>>>>>>> 351cf8f128ab6a68ba8aff57bdaac8aa213f72e9
cript = elGamal_encr(mensagem1, mensagem2, curva, publickey_1, publickey_2)
elGamal_decr(cript, curva, secretkey)