def to_rna(dna_strand):
    rna_strand = ""
    kv = {
        'G' : 'C',
        'C' : 'G',
        'T' : 'A',
        'A' : 'U'
    }
    for i in dna_strand:
        rna_strand = rna_strand + kv[i]

    return rna_strand
