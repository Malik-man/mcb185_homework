import sys
import mcb185

colorfile = sys.argv[1]  
R = int(sys.argv[2])     
G = int(sys.argv[3])     
B = int(sys.argv[4])   
  
def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d


dmin = 100000
color = None

with open(colorfile) as fp:
	for line in fp:
		word = line.split()
		val = word[2].split(',')
		r = int(val[0])
		g = int(val[1])
		b = int(val[2])
		d = abs(int(val[0]) - R) + abs(int(val[1]) - G) + abs(int(val[2]) - B)
		if d < dmin: 
			dmin = d
			color = word[0]
	print(color)