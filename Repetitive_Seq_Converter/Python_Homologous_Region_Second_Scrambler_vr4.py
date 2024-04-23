import random

# find homologous sequences between two sequences
def find_matching_regions(seq1, seq2, min_match_length=10):
    matching_regions = []
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)
    
    for i in range(len_seq1 - min_match_length + 1):
        for j in range(len_seq2 - min_match_length + 1):
            match_length = 0
            while (i + match_length < len_seq1 and
                   j + match_length < len_seq2 and
                   seq1[i + match_length] == seq2[j + match_length]):
                match_length += 1
            if match_length >= min_match_length:
                matching_regions.append((i, j, match_length))
    
    return matching_regions

def scramble_codons(sequence, start, end):
    new_sequence = list(sequence)
    for i in range(start, end, 3):
        codon = "".join(new_sequence[i:i+3])
        if codon in homologous_codons.values():
            amino_acid = [key for key, value in homologous_codons.items() if codon in value][0]
            synonymous_codons = [c for c in homologous_codons[amino_acid] if c != codon]
            new_codon = random.choice(synonymous_codons)
            new_sequence[i:i+3] = list(new_codon)
    return "".join(new_sequence)

# Sequences
sequence1 = ""
sequence2 = ""

# Find matching regions
matching_regions = find_matching_regions(sequence1, sequence2)

# check over sequences that are flagged for matches - codon scramble one sequence to make sure there isn't homology
homologous_codons = {
    'F': ['TTT', 'TTC'],
    'L': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'S': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Y': ['TAT', 'TAC'],
    '*': ['TAA', 'TAG', 'TGA'],
    'C': ['TGT', 'TGC'],
    'W': ['TGG'],
    'P': ['CCT', 'CCC', 'CCA', 'CCG'],
    'H': ['CAT', 'CAC'],
    'Q': ['CAA', 'CAG'],
    'R': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'I': ['ATT', 'ATC', 'ATA'],
    'M': ['ATG'],
    'T': ['ACT', 'ACC', 'ACA', 'ACG'],
    'N': ['AAT', 'AAC'],
    'K': ['AAA', 'AAG'],
    'V': ['GTT', 'GTC', 'GTA', 'GTG'],
    'A': ['GCT', 'GCC', 'GCA', 'GCG'],
    'D': ['GAT', 'GAC'],
    'E': ['GAA', 'GAG'],
    'G': ['GGT', 'GGC', 'GGA', 'GGG']
}

# Loop until the total number of matching regions is less than 100
while len(matching_regions) >= 100:
    # Scramble sequence1
    new_sequence1 = sequence1
    for region in matching_regions:
        start = region[0]
        end = start + region[2]
        new_sequence1 = scramble_codons(new_sequence1, start, end)
    
    # Find matching regions again
    matching_regions = find_matching_regions(new_sequence1, sequence2)

# Print the results
if matching_regions:
    print("Matching Regions:")
    for region in matching_regions:
        print("Sequence 1 Start:", region[0], "Sequence 2 Start:", region[1], "Length:", region[2])
