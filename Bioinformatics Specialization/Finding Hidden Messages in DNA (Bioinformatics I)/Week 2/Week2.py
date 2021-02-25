# Skew array - keeps track of total no of occurrences of C and G encountered so far in Genome

""" 
Genome = GAGCCACCGCGATA
"""


import collections
import itertools


def SkewArray(Genome):
    Skew = [0]
    for i in range(len(Genome)):
        if Genome[i] == 'C':
            Skew.append(Skew[i] - 1)
        elif Genome[i] == 'G':
            Skew.append(Skew[i] + 1)
        else:
            Skew.append(Skew[i])
    return Skew


data = (SkewArray(Genome))
s = ' '.join([str(pos) for pos in data])
print(s)

# Minimum Skew Problem - Find a position in a genome where the skew diagram attains a minimum
# returns all integer(s) i minimizing Skewi (Genome) among all values of i (from 0 to |Genome|).
# uses SkewArray

""" 
Genome = TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT
"""


def MinimumSkew(Genome):
    positions = []  # output variable
    array = SkewArray(Genome)
    count = 0
    minarray = min(array)
    for i in array:
        if i == minarray:
            positions.append(count)
        count += 1
    return positions


data = (MinimumSkew(Genome))
s = ' '.join([str(pos) for pos in data])
print(s)

# Hamming distance - The number of mismatches between strings p and q is called the Hamming distance
# between these strings and is denoted HammingDistance(p, q)

""" 
p = "GGGCCGTTGGT"
q = "GGACCGTTGAC"
"""


def HammingDistance(p, q):
    distance = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1
    return distance


print(HammingDistance(p, q))

# Approximate Pattern Matching - We say that a k-mer Pattern appears as a substring of Text with
# at most d mismatches if there is some k-mer substring Pattern' of Text having
# d or fewer mismatches with Pattern, i.e., HammingDistance(Pattern, Pattern') ≤ d.
# Our observation that a DnaA box may appear with slight variations leads to the
# following generalization of the Pattern Matching Problem
# uses hamming distance

""" 
Text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
Pattern = "ATTCTGGA"
d = 3
"""


def ApproximatePatternMatching(Text, Pattern, d):
    positions = []
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Text[i:i+len(Pattern)], Pattern) <= d:
            positions.append(i)
    return positions
# (compute Counti = print(len(ApproximatePatternMatching('Text', 'Pattern', d))))


print(*ApproximatePatternMatching(Text, Pattern, d))

# Approximate Pattern Count - Computing Countd(Text, Pattern) simply requires us to compute
# the Hamming distance between Pattern and every k-mer substring of Text
# uses Hamming Distance

""" 
Text = "TTTAGAGCCTTCAGAGG"
Pattern = "GAGG"
d = 2
"""


def ApproximatePatternCount(Pattern, Text, d):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Pattern, Text[i:i+len(Pattern)]) <= d:
            count += 1
    return count


print(ApproximatePatternCount(Pattern, Text, d))

# Frequent words with mismatches - A most frequent k-mer with up to d mismatches in Text is
# simply a string Pattern maximizing Countd(Text, Pattern) among all k-mers
# Uses PermuteMotifOnce,PermuteMotifDistanceTimes

""" 
from collections import defaultdict
import itertools

Genome = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
d = 1 
"""


def FrequentWordsMismatch(Genome, k, d):
    aprox_frq_words = []
    frequencies = defaultdict(lambda: 0)
    # all existent kmers with d mismatches of current kmer in genome
    for index in range(len(Genome) - k + 1):
        curr_kmer_and_neighbors = PermuteMotifDistanceTimes(Genome[index: index + k], d)
        for kmer in curr_kmer_and_neighbors:
            frequencies[kmer] += 1

    for kmer in frequencies:
        if frequencies[kmer] == max(frequencies.values()):
            aprox_frq_words.append(kmer)
    return aprox_frq_words


def PermuteMotifOnce(motif, alphabet={"A", "C", "G", "T"}):
    """
    Gets all strings within hamming distance 1 of motif and returns it as a
    list.
    """

    return list(set(itertools.chain.from_iterable([[
        motif[:pos] + nucleotide + motif[pos + 1:] for
        nucleotide in alphabet] for
        pos in range(len(motif))])))


def PermuteMotifDistanceTimes(motif, d):
    workingSet = {motif}
    for _ in range(d):
        workingSet = set(itertools.chain.from_iterable(map(PermuteMotifOnce, workingSet)))
    return list(workingSet)

# Mismatches and reverse complements - account for both mismatches and reverse complements.
# Recall that Patternrc refers to the reverse complement of Pattern.
# Output: All k-mers Pattern maximizing the sum Countd(Text, Pattern)+ Countd(Text, Patternrc)
# over all possible k-mers.
# uses Patterntonumber,Numbertopattern,PatternMatching,Hammingdistance,ReverseComplement


""" 
text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
d = 1
"""


def MismatchesAndReverseComplement(text, k, d):
    frequencyarray = {}
    rev_text = ReverseComplement(text)
    for i in range(0, 4**k):
        frequencyarray[i] = 0
    for i in frequencyarray:
        count, r_count = 0, 0
        count = PatternMatching(text, NumberToPattern(i, k), d)
        r_count = PatternMatching(rev_text, NumberToPattern(i, k), d)
        frequencyarray[i] = count+r_count
    return frequencyarray


def PatternMatching(text, pat, d):
    count = 0
    for i in range(0, len(text)):
        p = text[i:i+len(pat)]
        if len(p) != len(pat):
            break
        if HammingDistance(p, pat) <= d:
            count = count+1
    return count


def PatternToNumber(pattern):
    if len(pattern) == 0:
        return
    SymbolToNumber = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    if len(pattern) == 1:
        return SymbolToNumber[pattern]
    n = len(pattern)
    symbol = pattern[n-1]
    prefix = pattern[:n-1]
    return (4*PatternToNumber(prefix)+SymbolToNumber[symbol])


def NumberToPattern(index, k):
    NumberToSymbol = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    if k == 1:
        return NumberToSymbol[index]
    prefix_index = index//4
    r = index % 4
    symbol = NumberToSymbol[r]
    return NumberToPattern(prefix_index, k-1)+symbol


def ReverseComplement(Pattern):
    return Pattern[::-1].replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c").upper()


approx_kmers = MismatchesAndReverseComplement(text, k, d)
for a in approx_kmers:
    if approx_kmers[a] == max(approx_kmers.values()):
        print(NumberToPattern(a, k), end=' ')


# Our idea for generating Neighbors(Pattern, d) is as follows. If we remove the first symbol of Pattern
# then we will obtain a (k − 1)-mer
# k-neighbors of any k-mer is an easy way of generating all kmers.


# Neighbors - find the d-neighbourhood of a string. Returns the collection of strings Neighbors(Pattern, d).


"""
Pattern = "GCCGTCTTA"
d = 3
"""


def Neighbors(Pattern, d):
    if d == 0:
        return Pattern
    if len(Pattern) == 1:
        return {"A", "C", "G", "T"}
    Neighborhood = []
    SuffixNeighbors = Neighbors(Pattern[1:], d)
    for Text in SuffixNeighbors:
        if HammingDistance(Pattern[1:], Text) < d:
            for x in {"A", "C", "G", "T"}:
                Neighborhood.append(x + Text)
        else:
            Neighborhood.append(Pattern[0] + Text)
    return Neighborhood
