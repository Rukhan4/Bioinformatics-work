# Median String - a fast algorithm for generating Motifs(Pattern,Dna), a collection of Motifs(Pattern,Dna) as a collection
# of kmers that minimize d(Pattern,Motifs) where d is the hamming distance
# uses  neighbors, hammingdistance

""" 
Dna = ['TTACCTTAAC', 
        'GATATCTGTC', 
        'ACGGCGTTCG', 
        'CCCTAAAGAG', 
        'CGTCAGAGGT']

k = 7
"""


def MedianString(Dna, k):

    def get_distance(Pattern, Text):
        n = len(Text)
        k = len(Pattern)
        min_distance = HammingDistance(Text[:k], Pattern)
        for i in range(n - k + 1):
            distance = HammingDistance(Text[i:i + k], Pattern)
            if distance < min_distance:
                min_distance = distance
        return min_distance

    def get_total_distance(Pattern, Dna):
        total_distance = 0
        for text in Dna:
            distance = get_distance(Pattern, text)
            total_distance += distance
        return total_distance

    kmers = Neighbors("A" * k, k)

    min_pattern = kmers[0]
    min_total_distance = get_total_distance(min_pattern, Dna)
    for pattern in kmers[1:]:
        total_distance = get_total_distance(pattern, Dna)
        if total_distance < min_total_distance:
            min_pattern = pattern
            min_total_distance = total_distance

    return min_pattern


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

# Convert to words - A simple function to convert a list of values to a line of values with no separators


def ConvertToWords(s):
    s = ' '.join([str(pos) for pos in s])
    return s


print(ConvertToWords(MedianString(Dna, k)))
