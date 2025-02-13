import math

# 10demo.py by malik

print("hello world") # greeting

import math 

print(1.5e-2)

print(1 + 4)

print(2 ** 2)

print(abs(-5))

print(pow(2, 2))

print(abs(-9))

print(math.factorial(3))

print(math.e)

print(0.1 * 3)

a = 3
b = 4
c = math.sqrt(a**2 + b **2)
print(c)

print(type(a), type (b), type(c), sep=', ', end='!\n')


def pythagorus(a, b):
		c = math.sqrt(a**2 + b**2)
		return c
hyp = pythagorus(2, 2)

print(hyp)

def circle_area(r): return math.pi * r**2
def rectange_area(w, h): return w * h

print(circle_area(1))
print(rectange_area(1,1))

s = 'hello world'

print(s, type(s))

a = 5+1
b = 6
if a == b:
	print ('a equals b')
print(a, b)

def if_even(x):
		if x % 2 == 0: return True 
		return False
		
print(if_even(8))
print(if_even(1))

c = a == b
print(c)
print(type(c))

if a < b: print('a < b')
elif a > b: print('a > b')
else: 		print('a == b')

if a > b or a < b: print('all things being equal, a and b are not')
if a > b and a < b: print('you are living in a strange world')
if not False: print(True)

a = 0.3 
b = 0.1 * 3 
if a < b: print('a < b')
elif a > b: print('a > b')
else:		print('a == b')

print(abs(a-b)) #5.55111515e-1.7
if abs(a-b) < 1e-9: print('close enough')

if math.isclose(a, b): print('close enough')

def silly(m, x, b):

	y = m * x + b
print(silly(2, 3, 4))


import math

limit = 100

for a in range(1,limit): 
	for b in range(a+1,limit):
		c = math.sqrt(a**2 + b**2)
		remainder = c%1
		if c%1 == 0: print(a,b,c)
		
import random

def advantage():
	roll1 = random.randint(1,20)
	roll2 = random.randint(1,20)
	if roll1 > roll2: return roll1
	return roll2
trials = 5 
dc = 5
success = 0

for i in range(trials):
	roll = random.randint(1,20)
	if roll >= dc: success += 1
	print(i,roll)
print(success/trials)

def celsius_to_farenheit(celsius):
	farenheit = (celsius * 9/5) + 32
	return farenheit 

for celsius in range (5):
	farenheit = celsius_to_farenheit(celsius)
	print(celsius_to_farenheit(celsius))
	
def is_integer(x):
	if x%1 == 0: return True 
	return False 
	
print(is_integer(5.2))

def complement(x):
	if x == a:
		print(t)
	if x == t:
		print(a)
	if x == c:
		print(g)
	if x == g:
		print(c)
	else: print('None')
		
	print(complement(c))

	


	
	