# Gibbs sampler - discards a single kmer from the current set of motifs at each iteration and decides to either keep or replace one
# continuously to generate a suboptimal solution particularly for different search problems with elusive motifs (local optimum)
# uses randommotifs, countwithpseudocounts,profilewithpseudocounts,profilegeneratingstring,normalize,weighteddie, pr,score,consensus,count
import random
random.seed(0)
""" 
Dna = ["CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA",
       "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
       "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
       "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
       "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]

k = 8
t = 5
N = 100
"""
Dna = []

with open("C:/Users/18687/Desktop/Bio Informatics/Bioinformatics specialization/dataset.txt", 'r') as file:
    k = int(file.readline().strip())  # moves throughout the rows
    t = int(file.readline().strip())
    N = int(file.readline().strip())
    for item in file.readlines():
        Dna.append(item.strip())

file.close()


def GibbsSampler(Dna, k, t, N):
    Motifs = RandomMotifs(Dna, k, t)
    BestMotifs = Motifs.copy()
    for _ in range(1, N):
        i = random.randint(0, t - 1)
        Profile_Motifs = []
        for f in range(0, t):
            if f != i:
                Profile_Motifs.append(Motifs[f])
        Profile = ProfileWithPseudocounts(Profile_Motifs)
        Mot = ProfileGeneratedString(Dna[i], Profile, k)
        Motifs = Profile_Motifs.copy()
        Motifs.insert(i, Mot)
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs


# Normalize - rescale a collection of probabilities so that they sum to 1(follows Laplace's rule of succession).
# It takes a dict Probabilities whose keys are kmers, values are probabilities of these kmers.
# It then divides each value in Probabilities by the sum of all values in Probabilities, returning the resulting dict.


def Normalize(Probabilities):
    sumd = sum(Probabilities.values())
    for key in Probabilities.keys():
        Probabilities[key] /= sumd
    return Probabilities

# Weighted die - takes a dict Probabilities whose keys are kmers and values are Prob of these Kmers.
# Returns a randomly chosen kmer key wrt values in Probabilities


def WeightedDie(Probabilities):
    kmer = ''
    num = random.uniform(0, 1)
    sumd = 0
    for key in Probabilities.keys():
        sumd += Probabilities[key]
        if num < sumd:
            kmer = key
            break
    return kmer

# Profile Generated String - returns a randomly generated kmer from Text whose probabilities are generated from Profile
# uses pr, normalize, weighteddie


def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {}
    for i in range(n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)

# Motifs - takes a profile Matrix Profile corresponding to a list of strings Dna as input and returns a list of the Profile most
# probable k-mers in each string from Dna
# Uses ProfileMostProbableKmer and Pr


def Motifs(Profile, Dna):
    motifs = []
    t = len(Dna)
    # May take in a k value here
    for i in range(t):
        motif = ProfileMostProbableKmer(Dna[i], k, Profile)
        motifs.append(motif)
    return motifs

# Random Motifs - choose a random kmer from each of t different strings Dna and returns a list of t strings which
# continuously iterates for as long as the score of the constructed motifs keep improving


def RandomMotifs(Dna, k, t):
    t = len(Dna)
    l = len(Dna[0])
    RandomMotif = []
    for i in range(t):
        r = random.randint(0, l-k)
        RandomMotif.append(Dna[i][r:r+k])
    return RandomMotif

# Randomized Motif Search - starts by generating a collection of random motifs using the RandomMotifs function which we set as the best
# scoring collection of motifs. It continuously runs until motif score stops improving.
# uses RandomMotifs, ProfileWithPseudocounts, Motifs, Score


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

# Repeated randomized motif search - finds best scoring motif
# uses randommotif, Profilewithpseudocounts,countwithpseudocounts,score,consensus,count,motifs,Pr,RandomizedMotifSearch


def RepeatedRandomizedMotifSearch(Dna, k, t):
    BestScore = float('inf')
    BestMotifs = []
    for _ in range(100):
        Motifs = RandomizedMotifSearch(Dna, k, t)
        CurrentScore = Score(Motifs)
        if CurrentScore < BestScore:
            BestScore = CurrentScore
            BestMotifs = Motifs
    return BestMotifs

# Profile most probable kmer - a kmer that was most likely to have been generated by Profile among all kmers in Text
# Uses Pr function


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

# Count with Pseudocounts - takes a list of strings Motifs as input and returns the count matrix of Motifs
# with pseudocounts as a dict of lists
# Similar to count matrix but it starts at 1 and not 0


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

# Probability - of finding a chosen kmer given the profile matrix


def Pr(Text, Profile):
    pro = 1
    for i in range(len(Text)):
        pro = pro*Profile[Text[i]][i]
    return pro
# Profile with Pseudocounts - takes a list of strings Motifs as input and returns the profile matrix of Motifs with pseudocount as a dict
# of lists
# uses Countwithpseudocounts


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

# Count - creates a dictionary with all the nucleotides and how much they are present in the j-th column of the Motif matrix


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

# Score - summing the number of symbols in the j-th column of Motifs that do not match the symbol in position j of the consensus string
# uses Consensus and Count matrix


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


print("\n".join(GibbsSampler(Dna, k, t, N)))

""" 
not sure why this call does not work - ValueError: Expected 3 got 2, however file reads:
15
20
2000
where it should be k,t,N respectively. 

if __name__ == "__main__":
    with open("C:/Users/18687/Desktop/Bio Informatics/Bioinformatics specialization/dataset.txt", 'r') as file:
        k, t, N = [int(a) for a in file.readline().strip()]
        Dna = []
        for _ in range(t):
            Dna.append(input())
    best_motifs = GibbsSampler(Dna, k, t, N)
    for _ in range(20):  # 20 random starts
        new = GibbsSampler(Dna, k, t, N)
        if Score(new) < Score(best_motifs):
            best_motifs = new[:]
    print(*best_motifs, sep='\n')
"""
