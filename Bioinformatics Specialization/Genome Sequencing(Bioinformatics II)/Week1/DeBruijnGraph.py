# DeBruijn graph
# In general, given a genome Text, PathGraphk(Text) is the path consisting of |Text| - k + 1 edges,
# where the i-th edge of this path is labeled by the i-th k-mer in Text and the i-th node of the path
# is labeled by the i-th (k - 1)-mer in Text. The de Bruijn graph DeBruijnk(Text) is formed
# by gluing identically labeled nodes in PathGraphk(Text).


Text = "AAGATTCTCTAAGA"
k = 4  # (nodes on the graph and hence adjacency list is length 3 from k-1)

 


def DeBruijnGraph(Text, k):
    k = k - 1
    adj = {}
    for i in range(len(Text) - k+1):
        kmer = Text[i: i+k]
        if kmer not in adj:
            adj[kmer] = []
        patt = Text[i+1: i+k+1]
        if len(patt) == k:
            adj[kmer].append(patt)
        else:
            del adj[kmer]  # delete

    adj = dict(sorted(adj.items()))
    formattedTxt = ""
    for key in adj:
        formattedTxt += key + " -> " + ",".join(adj[key]) + "\n"
    return formattedTxt


print(DeBruijnGraph(Text, k))

""" 
txt = (DeBruijnGraph(Text, k))
file = open(
    "C:/Users/18687/Desktop/Bio Informatics/Bioinformatics specialization/debruijngraphanswer.txt", mode="w")
file.write(txt)
file.close()
"""
