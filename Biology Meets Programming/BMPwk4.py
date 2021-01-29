# Count with Pseudocounts - takes a list of strings Motifs as input and returns the count matrix of Motifs
# with pseudocounts as a dict of lists
# Similar to count matrix but it starts at 1 and not 0

import random


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

# Greedy Motif Search With Pseudocounts - generates each profile matrix with pseudocounts
# uses score,consensus,Pr,ProfileMostProbableKmer, ProfileWithPseudocounts, CountWithPseudocounts


def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    BestMotifs = []
    for i in range(t):
        BestMotifs.append(Dna[i][:k])
    n = len(Dna[0])
    for i in range(n-k+1):
        Motifs = []
        Motifs.append(Dna[0][i:i+k])
        for j in range(1, t):
            P = ProfileWithPseudocounts(Motifs[0:j])
            Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

# Motifs - takes a profile Matrix Profile corresponding to a list of strings Dna as input and returns a list of the Profile most
# probable k-mers in each string from Dna
# Uses ProfileMostProbableKmer and Pr


def Motifs(Profile, Dna):
    motifs = []
    t = len(Dna)
    k = 4  # for a 4-mer string
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
    for _ in range(N):
        Motifs = RandomizedMotifSearch(Dna, k, t)
        CurrentScore = Score(Motifs)
        if CurrentScore < BestScore:
            BestScore = CurrentScore
            BestMotifs = Motifs
    return BestMotifs


BestMotifs = RepeatedRandomizedMotifSearch(Dna, k, t)

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

# Gibbs sampler - discards a single kmer from the current set of motifs at each iteration and decides to either keep or replace one
# continuously to generate a suboptimal solution particularly for different search problems with elusive motifs (local optimum)
# uses randommotifs, countwithpseudocounts,profilewithpseudocounts,profilegeneratingstring,normalize,weighteddie, pr,score,consensus,count


def GibbsSampler(Dna, k, t, N):
    BestMotifs = []
    Motifs = RandomMotifs(Dna, k, t)
    BestMotifs = Motifs
    for i in range(N):
        i = random.randint(0, t-1)
        new_Motif = []
        for k1 in range(t):
            if k1 != i:
                new_Motif.append(Motifs[k1])
        profile = ProfileWithPseudocounts(new_Motif)
        motif_i = ProfileGeneratedString(Dna[i], profile, k)
        Motifs[i] = motif_i
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs
