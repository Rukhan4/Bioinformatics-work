# AN ALTERNATIVE FUNCTION TO SOLVE GREEDYMOTIFSEARCHWITHPSEUDOCOUNTS


dna = []

with open("filedirectory", 'r') as file:
    k = int(file.readline().strip())  # moves throughout the rows
    t = int(file.readline().strip())
    for item in file.readlines():
        dna.append(item.strip())

file.close()


def greedy_motif_search_with_pseudocounts(dna, k, t):
    best_motifs = []
    for i in dna:
        best_motifs.append(i[0:k])
    for i in range(0, len(dna[0])-k+1):
        motif = (dna[0][i:i+k])
        motifs = []
        for j in range(1, t):
            motifs.append(motif)
            prof = profile(motifs)
            motif = profile_probable(dna[j], k, prof)
        motifs.append(motif)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    result = ""
    for i in best_motifs:
        result = result+" "+i
    result = result.strip()
    return result


def pr(pattern, profile):
    prob = 1.00
    for i in range(0, len(pattern)):
        line = profile[pattern[i]]
        # print(prob)
        # print(line[i])
        prob = prob*line[i]
    return prob


def score(motifs):
    score = 0
    for j in range(0, len(motifs[0])):
        nc = {"A": 0, "C": 0, "G": 0, "T": 0}
        for i in motifs:
            nc[i[j]] = nc[i[j]]+1
        score = score+(len(motifs)-max(nc.values()))
    return score


def profile_probable(string, k, profile):
    prob = -1
    k_mer = ""
    for i in range(0, len(string)-k+1):
        if pr(string[i:i+k], profile) > prob:
            prob = pr(string[i:i+k], profile)
            k_mer = string[i:i+k]
    return k_mer

# THE FUNCTIONALITY LIES IN INITIALIZING THE SET AT 1 INSTEAD OF 0 TO PRODUCE GREEDYMOTIFSEARCHWITHPSEUDOCOUNTS


def profile(motifs):
    zeros = [1]  # INITIALIZED AT 1
    for i in range(0, len(motifs[0])):
        zeros.append(0)
    profile = {"A": zeros[:], "C": zeros[:], "G": zeros[:], "T": zeros[:]}
    for j in range(0, len(motifs[0])):
        for i in motifs:
            (profile[i[j]])[j] = (profile[i[j]])[j]+1
    for i in "ACGT":
        for j in range(0, len(motifs[0])):
            profile[i][j] = profile[i][j]/len(motifs)
    return profile


print(greedy_motif_search_with_pseudocounts(dna, k, t))
