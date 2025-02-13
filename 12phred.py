import math

def qual_to_error(qual_char):
	Q = ord(qual_char) - 33 
	p = 10 **(Q/-10)
	return p

def error_to_qual(error):
	Q = -10 *math.log10(error)
	A = int(Q//1) + 33
	return chr(A)
	
print(qual_to_error('#'))
print(error_to_qual(0.3))
	