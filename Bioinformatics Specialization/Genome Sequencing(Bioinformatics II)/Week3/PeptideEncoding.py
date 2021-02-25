# Peptide Encoding - find substrings of a genome encoding a given amino acid sequence


from ProteinTranslation import ProteinTranslation

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
""" 
text = "ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
peptide = "MA"
"""


def ReverseComplement(Pattern):
    return Pattern[::-1].replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c").upper()


def Dna_To_Rna(string):
    return string.replace("T", "U")


def PeptideEncoding(genetic_code, text, peptide):
    substrings = []
    k = len(peptide) * 3
    for i in range(len(text)-k):
        kmer = text[i:i+k]
        kmer_transcribed = Dna_To_Rna(kmer)
        kmer_translated = ProteinTranslation(kmer_transcribed)
        compliment = ReverseComplement(kmer)
        compliment_transcribed = Dna_To_Rna(compliment)
        compliment_translated = ProteinTranslation(compliment_transcribed)
        if kmer_translated == peptide or compliment_translated == peptide:
            substrings.append(kmer)
    return substrings


if __name__ == "__main__":
    with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\peptideencoding.txt", "r") as file:
        print('\n'.join(PeptideEncoding(genetic_code, file.readline(), "CHKNYFNWEG")))
