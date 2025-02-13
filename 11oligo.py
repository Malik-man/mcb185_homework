import math 

def oligo_tm(a, c, t, g):
	total = a + c + t + g
	
	if total <= 13:
		tm = (a + t) * 2 + (g + c) * 4
	
	else: 
		tm = 64.9 + 41 * ((g + c - 16.4)/ total)
	return tm

print(oligo_tm(5, 7, 3, 4))
print(oligo_tm(2, 1, 5, 2))
print(oligo_tm(100, 200, 304, 45))
	
	
