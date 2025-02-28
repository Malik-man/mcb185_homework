import sys
import math

vals = []
for arg in sys.argv[1:]:
	i = float(arg)
	vals.append(float(arg))
	
def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini
	
def maximum(vals):
	maxi = vals[0]
	for val in vals[1:]:
		if val > maxi: maxi = val
	return maxi
	
total = 0
for v in vals:
    total += v

def standard_deviation(vals):
    n = len(vals)
    mean = (total/len(vals))

    sum_sq_diff = 0
    for val in vals:
        sum_sq_diff += (val - mean) ** 2  

    std_dev = math.sqrt(sum_sq_diff / n)  
    return std_dev

	
def median(vals):
	vals.sort() 
	mid = len(vals) // 2 
	for val in vals: 
		if len(vals) % 2 == 0:
			return (vals[mid] + vals[mid - 1])/2
		else: 
			return vals[mid]
	

print('median',median(vals))  
print('number of values',len(vals))
print('minimum values',minimum(vals))
print('maximum values',maximum(vals))
print('mean',total/len(vals))
print('standard deviation', standard_deviation(vals))