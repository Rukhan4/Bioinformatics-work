# Contig Generation - Generate the contigs(long,contiguous segments of the genome)
# from a collection of reads with imperfect coverage


def ContigsFromReads(patterns):
    contigs = []
    graph = DeBruijnFromKmers(patterns)
    paths = MaximalNonBranchingPaths(graph)
    for path in paths:
        contigs.append(GenomePathSpelledString(path))
    return contigs


def DeBruijnFromKmers(patterns):
    graph = {}
    for text in patterns:
        prefix = text[:-1]
        suffix = text[1:]
        graph.setdefault(prefix, [])
        graph[prefix].append(suffix)
    return graph


def Degree(graph):
    degree = {}
    for v in graph:
        # degree[v] = [indegree, outdegree]
        degree.setdefault(v, [0, 0])
        degree[v][1] += len(graph[v])
        for w in graph[v]:
            degree.setdefault(w, [0, 0])
            degree[w][0] += 1
    return degree


def MaximalNonBranchingPaths(graph):
    paths = []
    degree = Degree(graph)
    visited = []    # stores all the visited 1-in-1-out nodes
    for v in graph:
        if degree[v][0] != 1 or degree[v][1] != 1:  # if v is not a 1-in-1-out node
            visited.append(v)
            if degree[v][1] > 0:
                for w in graph[v]:
                    path = [v, w]
                    while degree[w][0] == 1 and degree[w][1] == 1:
                        visited.append(w)
                        w = graph[w][0]
                        path.append(w)
                    paths.append(path)

    for v in graph:
        if degree[v][0] == 1 and degree[v][1] == 1:
            if v not in visited:
                visited.append(v)
                w = graph[v][0]
                cycle = [v]
                while degree[w][0] == 1 and degree[w][1] == 1:
                    visited.append(w)
                    cycle.append(w)
                    if v == w:
                        break
                    w = graph[w][0]
                paths.append(cycle)
    return paths


def GenomePathSpelledString(patterns):
    text = patterns[0]
    for p in patterns[1:]:
        text += p[-1]
    return text


def ReadPatterns(file, num=False):
    numbers = []
    if num:
        numbers = file.readline().split()
        numbers = map(int, numbers)

    patterns = file.readlines()
    patterns = [p.strip() for p in patterns]
    if num:
        numbers.append(patterns)
        return numbers
    else:
        return patterns


with open("C:/Users/18687/Desktop/Bio Informatics/Bioinformatics specialization/contigs.txt", "r") as file:
    patterns = ReadPatterns(file)
    contigs = ContigsFromReads(patterns)
    print(' '.join(str(pos) for pos in contigs))

file.close()
