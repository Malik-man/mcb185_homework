import math
s = "hello world"
print(s)

i = int('42') #very important 
x = float('0.61803')
print(i * x)


s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)

print('hey "dude" \tdon\'t tell me what to do')

s3 = 'hello' + 'world'

PolyA = 'A' * 100

print(PolyA)
print(s3)

print(len(PolyA))

print(s2.upper())

print(s2)

print(s.replace('o', ''))
print(s.replace('o', '').replace('r', 'i'))

print(f'{math.e}')

print(f'{math.pi:.3f}')

print(f'{1e6 * math.pi:e}')


print(f'{"hello world":>40}')
print(f'{"hello world":=>40}')

print(f'{20:<10} {20}')

print('{} {:.10f}'.format('the number:', math.pi))

print('%s %.3f' % ('print if', math.pi))

seq = 'GAATTC'
print(seq[5], seq[-1])

for nt in seq:
	print(nt, end='-')
print()

for i in range(len(seq)):
    print(i, seq[i])
s = 'ABCDEFGHI'
print(s[1:5], s[0])

print(s, s[::], s[::1], s[::-4])

dna = 'ATGCTGCATGTA'
for i in range(0, len(dna), 3):
	codon = dna[i:i+3]
	print(i, codon)
	


nts = 'ACGT'
for i in range(len(nts)):
	print(i,nts[i])
	
print(list(enumerate(nts)))

names = ('adenien', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])
print(list(enumerate(names)))


for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)
	
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

stuff = []
stuff.append(3)
print(stuff)

alpha = 'ACDEFGHIKLMPQRSVW'
print(alpha)
aas = list(alpha)
print(aas)

text = 'good day									to you'
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split('k'))


s = '='.join(aas)
print(s)
s = ''.join(aas)
print(s)
if "A" in alpha: print(':D')


print('index G', alpha.index('G'))



print('find G', alpha.find('G'))
print('find Z', alpha.find('Z'))

import sys
import math

def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini
	
	
vals = []
for arg in sys.argv[1:]:
	i = float(arg)
	vals.append(float(arg))
	
