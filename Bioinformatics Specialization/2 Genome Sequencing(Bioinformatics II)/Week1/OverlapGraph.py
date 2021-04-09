# Overlap Graph Problem - returns the overlap graph in the form of an adjacency list(nodes and edges in any order)
# Doesnt need to account for repeated elements in Patterns

from collections import defaultdict

""" 
patterns = [
    "ATGCG",
    "GCATG",
    "CATGC",
    "AGGCA",
    "GGCAT",
    "GGCAC"
]

"""
file = open("C:/Users/18687/Desktop/Bio Informatics/Bioinformatics specialization/overlapgraph.txt", mode="r")
patterns = file.read().strip().splitlines()


def Overlap(patterns):
    # Default_factory, list is created with distinct objects
    adjacency_list = defaultdict(set)
    for patt in patterns:
        adjacency_list[patt[:-1]].add(patt)
    for patt in patterns:
        suffixes = adjacency_list[patt[1:]]
        if suffixes:
            print(patt + " -> " + ",".join(suffixes))
        else:
            continue


Overlap(patterns)
