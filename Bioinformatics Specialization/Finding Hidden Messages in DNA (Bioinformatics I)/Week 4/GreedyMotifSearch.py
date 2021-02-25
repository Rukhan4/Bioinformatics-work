# Greedy motif search - Output: A collection of strings BestMotifs resulting from applying
# GreedyMotifSearch(Dna, k, t). If at any step you find more than one Profile-most probable k-mer
# in a given string, use the one occurring first.
# uses score,profile,profilemostprobablekmer (updated)
""" 
k = 3
t = 5
Dna = [
"GGCGTTCAGGCA",
"AAGAATCAGTCA",
"CAAGGAGTTCGC",
"CACGTCAATCAC",
"CAATAATATTCG",
]
"""


def GreedyMotifSearch(Dna, k, t):
    bestmotifs = [string[:k]for string in Dna]
    for j in range(len(Dna[0])-k+1):
        motifs = [Dna[0][j:j+k]]
        for i in range(1, t):
            motifs += [profilemostprobablekmer(Dna[i], k, profile(motifs))]
        if score(motifs) < score(bestmotifs):
            bestmotifs = motifs
    return bestmotifs


def profile(motifs):
    transposed = [list(row) for row in zip(*motifs)]
    n = len(motifs)
    profile = {nucleotide: [i.count(nucleotide)/n for i in transposed] for nucleotide in 'ACGT'}
    return profile


def score(motifs):
    transposed = [list(row) for row in zip(*motifs)]
    counted = [[i.count(nucleotide) for nucleotide in 'ACGT'] for i in transposed]
    scored = sum([len(motifs)-max(i) for i in counted])
    return scored


def profilemostprobablekmer(text, k, profile):
    probability = []
    for i in range(len(text)-k+1):
        compute = 1
        for j in range(k):
            compute = compute*(profile[text[i+j]][j])
        probability.append(compute)
    idx = probability.index(max(probability))
    return text[idx:idx+k]


print((*GreedyMotifSearch(Dna, k, t)))  # Astericks converts list to string
