
k = 4

kmers = ["AAAT",

         "AATG",

         "ACCC",

         "ACGC",

         "ATAC",

         "ATCA",

         "ATGC",

         "CAAA",

         "CACC",

         "CATA",

         "CATC",

         "CCAG",

         "CCCA",

         "CGCT",

         "CTCA",

         "GCAT",

         "GCTC",

         "TACG",

         "TCAC",

         "TCAT",

         "TGCA"]


def k_universal_string_linear(k):
    values = 2 ** k
    patterns = [f'{x:0{k}b}' for x in range(values)]
    adj_list = DeBruijnFromKmers(patterns)
    cycle = EulerianCycle(adj_list)  # for extra question: linear
    text = PathToGenome(cycle)
    return text


def DeBruijnFromKmers(kmers):
    adj = {}
    for kmer in kmers:
        key = kmer[:-1]
        if key not in adj:
            adj[key] = []
        adj[key].append(kmer[1:])

    adj = dict(sorted(adj.items()))
    return adj


def PathToGenome(path):
    string = path[0]
    string += "".join([x[-1] for x in path[1:]])
    return string


def EulerianCycle(graph):
    cycle = []
    stack = []
    new_start = list(graph.keys())[0]
    stack.append(new_start)
    while len(stack) != 0:  # while the graph is not empty
        start = stack[-1]  # the start node is the top of the stack
        if graph.get(start):  # if it exists in the graph
            end = graph[start][0]  # the end node is found with adjacency list
            stack.append(end)  # add it to the top of the stack
            graph[start].remove(end)  # remove it from the graph
        else:  # if the start node is not in the graph
            # add the start node to the cycle AND remove it from the stack
            cycle.append(stack.pop())

    num_edges = sum((len(v) for v in graph.values()))
    if num_edges == 0:  # check to see if all edges were visited
        return list(reversed(cycle))  # the cycle is in the reverse order
    return []


print(k_universal_string_linear(k))
