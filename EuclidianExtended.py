def euclidian(a, b):
	r = a
	r1 = b
	u = 1
	v = 0
	u1 = 0
	v1 = 1

	while r1 != 0:
		q = r // r1
		rs = r
		us = u
		vs = v
		r = r1
		u = u1
		v = v1
		r1 = rs - q * r1
		u1 = us - q * u
		v1 = vs - q * v1
	
	return v