'''
CODE CHALLENGE: Solve the Converting a Peptide Vector into a Peptide Problem.
Given: A space-delimited binary vector P.
Return: An amino acid string whose binary peptide vector matches P. For masses with more than one amino acid, any choice may be used.
'''

from collections import defaultdict

massTable = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 'I': 113, 'H': 137, 'K': 128, 'M': 131,
             'L': 113, 'N': 114, 'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163, 'X': 4, 'Z': 5}


def get_mass(peptide):
    if len(peptide) == 0:
        return 0
    return sum([massTable[pep] for pep in peptide])


def spectrum_graph(Spectrum):
    Spectrum = sorted(Spectrum)
    specGraph = defaultdict(list)
    weighGraph = defaultdict(list)
    for i in range(len(Spectrum)):
        for j in range(i+1, len(Spectrum)):
            if Spectrum[j]-Spectrum[i] in massTable.values():
                aa = [key for key, val in massTable.items() if val == Spectrum[j]-Spectrum[i]]
                specGraph[Spectrum[i]].append(Spectrum[j])
                weighGraph[Spectrum[i]].append(aa[0])
    specGraph[max(Spectrum)] = []
    weighGraph[max(Spectrum)] = []
    return specGraph, weighGraph


def depthFirstPaths(graph, s):
    edgeTo = dict((key, None) for key in graph.keys())
    marked = dict((key, False) for key in graph.keys())
    postorder = []
    edgeTo, marked, postorder = dfs(graph, s, edgeTo, marked, postorder)
    return edgeTo, marked, postorder


def dfs(tree, v, edgeTo, marked, count):
    count = 1
    marked[v] = True
    for w in tree[v]:
        if not marked[w]:
            edgeTo[w] = v
            edgeTo, marked, count = dfs(tree, w, edgeTo, marked, count)
    return edgeTo, marked, count


def pathTo(graph, weights, s, v, edgeTo):
    stack = []
    weightstack = []
    w = edgeTo[v]
    stack.append(v)
    weightstack.append(weights[w][graph[w].index(v)])
    while w != s:
        stack.append(w)
        v = w
        w = edgeTo[v]
        weightstack.append(weights[w][graph[w].index(v)])
    stack.append(s)
    return stack[::-1], ''.join(weightstack[::-1])


def from_peptide_vector(vector):
    mass = [i+1 for i in range(len(vector)) if vector[i] == 1]
    mass = [0] + mass
    return mass


def ideal_spectrum(peptide):
    idealPrefixSpec = []
    for i in range(1, len(peptide)+1):
        idealPrefixSpec.append(get_mass(peptide[:i]))
    return idealPrefixSpec


def decode_ideal_spec(spec):
    specGraph, weighGraph = spectrum_graph(spec)
    source = min(spec)
    sink = max(spec)
    edgeTo, marked, postorder = depthFirstPaths(specGraph, source)
    paths, peptides = pathTo(specGraph, weighGraph, source, sink, edgeTo)
    peptide = []
    for i in range(len(paths)-1):
        peptide.append(weighGraph[paths[i]][specGraph[paths[i]].index(paths[i+1])])
    return ''.join(peptide)


with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\vectortopeptide.txt", "r") as input_file:
    res = input_file.read()
    pepvector = list(map(int, res.split()))

spec = from_peptide_vector(pepvector)
print(decode_ideal_spec(spec))
