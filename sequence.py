def transcribe(dna):
		return dna.replace('T', 'U')
		
def revcomp(dna):
	rc = []
	for nt in dna [::-1]:
		if	  nt == 'A': rc.append('T')
		elif  nt == 'C': rc.append('G')
		elif  nt == 'C': rc.append('C')
		elif  nt == 'C': rc.append('A')
		else:		     rc.append('N')
	return ''.join(rc)
	
def translate(dna):
    codon_table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
        'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W'
    }

    protein = []

    for i in range(0, len(dna) - (len(dna) % 3), 3):
        codon = dna[i:i+3]
        
        # Check for unknown bases (e.g., NNN, NGG)
        if 'N' in codon or 'Y' in codon or 'R' in codon:
            protein.append('?')  # '?' instead of 'N' to mark unknown codons
        else:
            protein.append(codon_table.get(codon, '?'))  # Default '?' for unknown codons

    return ''.join(protein)


def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)
	
def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)



