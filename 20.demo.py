import math 

t = 1, 2 # this is a tuple 
print(t)
print(type(t))

person = 'Steve', 21, 57891.50 # name, age
print(person)

def midpoint(x1, y1, x2, y2):
	x = (x1 + x2) / 2
	y = (y1 + y2) / 2
	return x, y
print(midpoint(1, 2, 3, 4))

print(midpoint(1, 2, 3, 4))
m = midpoint(1, 2, 3, 4)
mx, my = midpoint(1, 2, 3, 4)
print(mx, my)

print(m[0], m[1])

i = 0 
while i < 3:
	i = i + 1
	print('hey', i)
	if i == 3: break
	
basket = "milk", "eggs", "bread"
for thing in basket:
	print(thing)
	
for i in range(7):
	if i % 2 == 0: print(i, "is even")
	else:			print(i, 'is odd')

