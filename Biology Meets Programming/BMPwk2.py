"""
NOT RUN
"""

# Symbol array - helps to count the number of C in a window of Extended Genome, along with Pattern Count. Takes strings Genome and symbol
# as input and returns the symbol array of Genome corresponding to symbol.
# uses patterncount


def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):  # i-th element is the number of occurrences of the symbol in window length len(genome)//2 starting at pos i of Extended Genome
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array


def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

# FasterSymbol array - takes genome and symbol but computes it quicker by using a better for loop
# uses patterncount


def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]

    # look at the first half of Genome to compute first array value
    array[0] = PatternCount(symbol, Genome[0:n//2])

    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i-1]

        # the current array value can differ from the previous array value by at most 1
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array


# Skew array - keeps track of total no of occurrences of C and G encountered so far in Genome

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

# Minimum skew - location where skew diagram obtains a minimum(location of ori)
# uses skewarray


def MinimumSkew(Genome):
    positions = []  # output variable
    array = SkewArray(Genome)
    positions = []
    count = 0
    minarray = min(array)
    for i in array:
        if i == minarray:
            positions.append(count)
        count += 1
    return positions

# Hamming distance - pos i in kmers p and q is a mismatch if the symbols at pos i of the 2 strings are not the same
# Total no. of mismatches bt strings p and q = hamming distance bt the strings.


def HammingDistance(p, q):
    count = 0
    for x, y in zip(p, q):
        if x != y:
            count += 1
    return count

# Approximate Pattern Matching - finf all approx occurrences of a pattern in a string with at most d mismatches
# uses hammingdistance


def ApproximatePatternMatching(Text, Pattern, d):
    positions = []
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Text[i:i+len(Pattern)], Pattern) <= d:
            positions.append(i)
    return positions

# Approximate pattern count - find DnaA boxes by identifying frequent kmers, with d possible mismatches.


def ApproximatePatternCount(Pattern, Text, d):
    count = 0  # initialize count variable
    for i in range(len(Text)-len(Pattern)+1):
        if HammingDistance(Pattern, Text[i:i+len(Pattern)]) <= d:
            count += 1
    return count
 
