"""
NOT RUN
"""

# Pattern count - finds all occurences of a Pattern in a Text of bases.


def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

# Frequency Map -  computes the frequency map of a given string Text and integer k, returns a dictionary of each supplied k-mer value
# eg. 3 and the provided Text


def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
        for j in range(n-k+1):
            if Text[j:j+k] == Pattern:
                freq[Pattern] = freq[Pattern] + 1
    return freq

# Frequent Words - list of all keys that have value in freq == m
# uses frequencymap


def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            pattern = key
            words.append(pattern)
    return words

# Reverse Complement - finds the complement strand of a DNA strand
# uses reverse,complement


def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern)  # reverse all letters in a string
    Pattern = Complement(Pattern)  # complement each letter in a string
    return Pattern
    # OR return(Pattern[::-1].replace("A","t").replace("T","a").replace("G","c").replace("C","g").upper())


def Reverse(Pattern):
    rev = ''.join(reversed(Pattern))
    return rev
    # OR return Pattern[::-1]


def Complement(Pattern):
    basepairs = {"A": "T", "G": "C", "T": "A", "C": "G"}
    complement = ""
    for base in Pattern:
        complement += basepairs.get(base)  # Get returns value for key
    return complement

# Pattern Matching - find all occurrences of a pattern in a string


def PatternMatching(Pattern, Genome):
    positions = []
    for i in range(len(Genome)-len(Pattern)+1):
        if Pattern == Genome[i:i+len(Pattern)]:
            positions.append(i)
    return positions
