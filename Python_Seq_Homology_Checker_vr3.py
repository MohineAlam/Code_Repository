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

# Print the results
if matching_regions:
    print("Matching Regions:")
    for region in matching_regions:
        print("Sequence 1 Start:", region[0], "Sequence 2 Start:", region[1], "Length:", region[2])
    