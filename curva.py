class CurvaEliptica:
	def __init__(self, a, b, p):
		
		if a < 0:
			while a < 0:
				a += p

		if a >= p:
			a = a % p		

		if b < 0:
			while b < 0:
				b += p	

		if b >= p:
			b = b % p		


		self.a = a
		self.b = b
		self.p = p 		