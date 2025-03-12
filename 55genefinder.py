import mcb185
import sys
import sequence


# Starting in frame 0

def frames(gene, mmsize):
	stops = ('TAG', 'TAA', 'TGA')
	keep = []
	
	for i in range(0, 3):
		seq = gene[i:] # shifts the reading frame to start at position i
		position = 0 # keeps track of out position 1 in the nucleotide 
	
# Find a start codon

		while position < len(seq):			# makes sure we don't run of the sequence
			if seq[position:position + 3] != 'ATG':
				position += 3 # if the current position is not ATG skip ahead 
				continue
			
# Find a stop codon
			
			for j in range(position, len(seq), 3):
				codon = seq[j:j + 3]
				if codon in stops: break # break the loop if we find a stop codon 
			
# keep the middle part
			
			length = j - position + 1 # does not include the last nucleotide so we add +1 
			if length > mmsize:
				coords = (position, j)
				keep.append(coords) # if the length is less than the mmsize we keep
		
			position = j
	return keep

# main function

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	words = defline.split()
	revseq = sequence.revcomp(seq)

# forward strand
	
	for start, end in frames(seq, int(sys.argv[2])):
		print(f"{start} {end}")
	
# reverse strand
	
	for start, end in frames(revseq, int(sys.argv[2])):
		position = len(seq) - end  - 2
		stop = len(seq) - begin
		print(f"{start} {end}")
