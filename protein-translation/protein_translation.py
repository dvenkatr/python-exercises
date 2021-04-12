def proteins(strand):
    proteins = []
    kv = {
        "AUG" : "Methionine",
        "UUU" : "Phenylalanine", 
        "UUC" : "Phenylalanine",
        "UUA" : "Leucine",
        "UUG" : "Leucine",
        "UCU" : "Serine",
        "UCC" : "Serine",
        "UCA" : "Serine",
        "UCG" : "Serine",
        "UAU" : "Tyrosine",
        "UAC" : "Tyrosine",
        "UGU" : "Cysteine",
        "UGC" : "Cysteine",
        "UGG" : "Tryptophan",
        # "UAA" : "STOP",
        # "UAG" : "STOP",
        # "UGA" : "STOP"
    }

    while(len(strand) != 0):
        codon = strand[:3]
        print(codon)
        if (codon == "UAA" or codon == "UAG" or codon == "UGA"):
            break
        else: 
            print(kv.get(codon))
            proteins.append(kv.get(codon))
            strand = strand[3:]
            print(strand)
    return proteins