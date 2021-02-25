# DeBruijn Graph from k-mers - returns the adjacency list of the de Bruijn graph for Patterns.

"""
kmers = [
    "GAGG",
    "CAGG",
    "GGGG",
    "GGGA",
    "CAGG",
    "AGGG",
    "GGAG"
]

kmers = ""
with open("C:/Users/18687/Desktop/Bio Informatics/Bioinformatics specialization/debruijnfromkmers.txt", "r") as file:
    kmers = file.readlines()

file.close()
"""


def DeBruijnFromKmers(kmers):
    adj = {}
    for kmer in kmers:
        key = kmer[:-1]
        if key not in adj:
            adj[key] = []
        adj[key].append(kmer[1:])

    adj = dict(sorted(adj.items()))
    formattedTxt = ""
    for key in adj:
        formattedTxt += key + " -> " + ",".join(adj[key])
    return formattedTxt


""" 
txt = (DeBruijnFromKmers(kmers))
file = open(
    "C:/Users/18687/Desktop/Bio Informatics/Bioinformatics specialization/debruijnfromkmersanswer.txt", mode="w")
file.write(txt)
file.close()
"""
if __name__ == "__main__":
    DeBruijnFromKmers(kmers)
