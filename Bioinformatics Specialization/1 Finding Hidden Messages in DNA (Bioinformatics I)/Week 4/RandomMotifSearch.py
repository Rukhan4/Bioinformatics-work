# Repeated Randomized Motif Search - Returns Best Motifs results from running the algorithm 1000 times, using pseudocounts
# this process iterates repeatedly in hopes of reducing the score until a minimum is achieved
# uses randomizedmotifsearch, randommotifs, Profilewithpseudocounts,motifs,score,countwithpseudocounts,consensus,pr,Profilemostprobablekmer and random module

import random
random.seed(0)
"""
Dna = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
       "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
       "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
       "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
       "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]

k = 8

t = 5

"""
Dna = []

with open("C:/Users/18687/Desktop/Bio Informatics/Bioinformatics specialization/dataset.txt", 'r') as file:
    k = int(file.readline().strip())  # moves throughout the rows
    t = int(file.readline().strip())
    N = int(file.readline().strip())
    for item in file.readlines():
        Dna.append(item.strip())

file.close()


def RepeatedRandomizedMotifSearch(Dna, k, t):
    BestScore = float('inf')
    BestMotifs = []
    for _ in range(N):
        Motifs = RandomizedMotifSearch(Dna, k, t)
        CurrentScore = Score(Motifs)
        if CurrentScore < BestScore:
            BestScore = CurrentScore
            BestMotifs = Motifs
    return BestMotifs


def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M

    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs


def Motifs(Profile, Dna):
    motifs = []
    t = len(Dna)
    # May take in a k value here
    for i in range(t):
        motif = ProfileMostProbableKmer(Dna[i], k, Profile)
        motifs.append(motif)
    return motifs


def RandomMotifs(Dna, k, t):
    t = len(Dna)
    l = len(Dna[0])
    RandomMotif = []
    for i in range(t):
        r = random.randint(0, l-k)
        RandomMotif.append(Dna[i][r:r+k])
    return RandomMotif


def Score(Motifs):
    count = Count(Motifs)
    consensus = Consensus(Motifs)
    letters = {'A', 'C', 'T', 'G'}
    running_sum = 0
    for i, letter in enumerate(consensus):
        losers = letters - set(letter)
        for remaining_letter in losers:
            running_sum += count[remaining_letter][i]
    return running_sum


def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus


def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in 'ACGT':
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count


def Pr(Text, Profile):
    pro = 1
    for i in range(len(Text)):
        pro = pro*Profile[Text[i]][i]
    return pro


def ProfileMostProbableKmer(text, k, profile):
    n = len(text)
    m = 0
    x = text[1:k]
    for i in range(n-k+1):
        Pattern = text[i:i+k]
        p = Pr(Pattern, profile)
        if p > m:
            m = p
            x = Pattern
    return x


def CountWithPseudocounts(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(1)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count


def ProfileWithPseudocounts(Motifs):
    k = len(Motifs[0])
    profile = {}
    count = CountWithPseudocounts(Motifs)
    total = 0
    for symbol in "ACGT":
        total += count[symbol][0]
        for k, v in count.items():
            profile[k] = [x/total for x in v]
    return profile


print("\n".join(RepeatedRandomizedMotifSearch(Dna, k, t)))
