import mcb185
import gzip 
import sys
import sequence 

seq = ""

with gzip.open("/Users/maliknadir/Code/MCB185/data/GCF_000005845.2_ASM584v2_genomic.fna.gz", 'rt') as fp:
    for line in fp:
        if not line.startswith(">"):  
            seq += line.strip()  

w = 1000
s = 100

g = seq[:w].count('G')
c = seq[:w].count('C')

   
   
for i in range(1, len(seq) - w + 1, s):
    if seq[i - 1] == 'G': g -= 1
    elif seq[i - 1] == 'C': c -= 1
    if seq[i + w - 1] == 'G': g += 1
    elif seq[i + w - 1] == 'C': c += 1

      
print(i, sequence.gc_comp(seq[i : i + w]), sequence.gc_skew(g, c))
