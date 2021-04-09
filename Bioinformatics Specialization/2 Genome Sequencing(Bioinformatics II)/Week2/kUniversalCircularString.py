# k Universal Circular String Problem - Find the Eulerian Cycle in the DeBruijn Graph for a BinaryStringk
# where the nodes represent all possible binary (k-1)mers and a directed edge connects (k-1)mer Pattern
# to (k-1)mer in the Pattern2, if there exists a kmer whose prefix is Pattern and Suffix is Pattern2
from StringReconstruction import PathToGenome
from EulerianCycle import EulerianCycle
from itertools import product

k = 9


def DeBruijnFromKmers(kmers):
    adj = {}
    for kmer in kmers:
        key = kmer[:-1]
        if key not in adj:
            adj[key] = []
        adj[key].append(kmer[1:])

    adj = dict(sorted(adj.items()))
    return adj


def StringReconstruction(patterns):
    adj_list = DeBruijnFromKmers(patterns)
    path = EulerianCycle(adj_list)
    text = PathToGenome(path)
    return text


def kUniversalCircularString(k):
    universal_dict = {}
    for kmer in [''.join(item) for item in product('01', repeat=k)]:  # Finds all binary outputs for k
        if kmer[:-1] in universal_dict:
            universal_dict[kmer[:-1]].append(kmer[1:])
        else:
            universal_dict[kmer[:-1]] = [kmer[1:]]
    return universal_dict


path = EulerianCycle(kUniversalCircularString(k))
print(''.join([item[0] for item in path[:-1]]))  # Since it is a cycle
