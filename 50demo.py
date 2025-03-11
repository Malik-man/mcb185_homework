import random 
import time

s = {'A', 'C', 'G'} #A set is a mutable container, but all of the elements are unique and the elements are not ordered.
#print(s)

s.add('T')
#print(s)

#print(s[2]) #Since it doesn't have order, the following code generates an error:

def random_names(n, k):
		klist = list()
		kset = set()
		for _ in range(n):
				kmer = ''.join(random.choices('ACGT', k=k))
				klist.append(kmer)
				kset.add(kmer)
		return klist, kset

for size in range(1000, 10000, 1000):
	
			list1, set1 = random_names(size, 10)
			list2, set2 = random_names(size, 10)
			
			t0 = time.time()
			for name1 in list1: 
					if name1 in list2: pass
			t1 = time.time()
			list_time = t1 - t0
			
			t0 = time.time()
			for name1 in list1:
					if name1 in set2: pass
			t1 = time.time()
			set_time = t1 - t0
			
			#print(list_time, set_time, list_time/set_time)
			
d = {'dog': 'woof', 'cat': 'meow'}
print(d)

#Both dictionaries and sets are displayed with curly brackets. 
#The difference is that dictionaries are key:value pairs, whereas sets are just values. 
#Like sets, dictionaries are also very efficient for lookups.

#To add new items to a dictionary, assign a new key:value pair.

d['pig'] = 'oink'
print(d)

#To change the value of an item, access it with its key.

d['cat'] = 'mew'


del d['dog']
print(d)


count = {}

seq = "ACGTAGCTAGGCTAAGGCTA"  # Example DNA sequence

for nt in seq:
    if nt not in count:
        count[nt] = 0
    count[nt] += 1

# Print results
for nt, n in count.items():
    print(nt, n)

#python3 51countgff.py ecoli.gff.gz | sort
'The first line below sorts the output by the feature name.'
#python3 51countgff.py ecoli.gff.gz | sort -n -k 2
'The second line sorts the second column -k 2 numerically -n'
#python3 51countgff.py ecoli.gff.gz | sort -nk2
'The two options can be collapsed as -nk2.'
'The k must come after the n because it has an argument, so -kn2 would not work.'

import itertools
for nts in itertools.product('ACGT', repeat=2):
    print(nts)
