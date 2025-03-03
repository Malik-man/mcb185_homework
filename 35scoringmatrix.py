import sys

nucleotides = sys.argv[1]
match_score = sys.argv[2]
mismatch_score = sys.argv[3]

print("   ", end = "")
for nt in nucleotides:
	print(nt, end="  ")
print()

for nt1 in nucleotides:
	print(nt1, end =" ")
	for nt2 in nucleotides:
		if nt1 == nt2 : print(match_score, end = ' ') 
		else: print(mismatch_score, end = ' ')
	print()
	
		
	


