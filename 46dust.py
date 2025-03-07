import sys
import sequence
import mcb185
import math


def shan_ent(a, c, g, t):
    total = a + c + g + t
    if total == 0:  
        return 0
    
    probs = [a/total, c/total, g/total, t/total]
    ent = -sum(p * math.log2(p) for p in probs if p > 0) 
    return ent

file = sys.argv[1]
window_size = int(sys.argv[2])
ent_thresh = float(sys.argv[3])

for defline, seq in mcb185.read_fasta(file):
    nts = list(seq)

    for i in range(0, len(seq) - window_size + 1):
        subseq = seq[i:i + window_size]
        acount = subseq.count('A')
        ccount = subseq.count('C')
        gcount = subseq.count('G')
        tcount = subseq.count('T')

        ent = shan_ent(acount, ccount, gcount, tcount)

        if ent < ent_thresh:
            for j in range(i, i + window_size):
                nts[j] = 'N'  

    final_seq = ''.join(nts)
    print(f'>{defline}')
    
    
    for i in range(0, len(final_seq), 60):
    	print(final_seq[i:i+60])
