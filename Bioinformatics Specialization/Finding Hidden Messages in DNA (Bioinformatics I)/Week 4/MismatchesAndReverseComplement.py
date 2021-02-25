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

# Hamming distance - The number of mismatches between strings p and q is called the Hamming distance
# between these strings and is denoted HammingDistance(p, q)


def HammingDistance(p, q):
    distance = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1
    return distance


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
