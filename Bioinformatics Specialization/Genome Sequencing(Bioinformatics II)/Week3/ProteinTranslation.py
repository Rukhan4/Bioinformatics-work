# Protein Translation - translate an RNA string into an amino acid string
# requires array of Genetic Code

# Genetic code array
genetic_code = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
                "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
                "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
                "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
                "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
                "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
                "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
                "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
                "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
                "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
                "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
                "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
                "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
                "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
                "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

rna_string = "CCAAGAACAGAUAUCAAU"


def ProteinTranslation(rna_string):
    codons = []
    for i in range(0, len(rna_string), 3):
        if i != "*":
            codons.append(rna_string[i:i+3])
    proteins = ''.join([genetic_code[codon] for codon in codons])
    return proteins


if __name__ == "__main__":

    print(ProteinTranslation(rna_string))
