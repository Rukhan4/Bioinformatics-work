# String Reconstruction - Takes in an integer k followed by a list of kmers Patterns to return a
# String Text with kmer composition equal to Patterns


import operator

with open("C:/Users/18687/Desktop/Bio Informatics/Bioinformatics specialization/stringreconstruction.txt", "r") as file:
    patterns = file.read().strip().splitlines()

file.close()


def get_balance(adj_list):
    balance = {}
    for start in adj_list.keys():
        if not balance.get(start):
            balance[start] = 0
        for end in adj_list[start]:
            balance[start] -= 1
            if balance.get(end):
                balance[end] += 1
            else:
                balance[end] = 1
    return balance


def EulerianPath(graph):
    path = []
    stack = []
    balance = get_balance(graph)
    stack.append(min(balance.items(), key=operator.itemgetter(1))[0])
    while len(stack) != 0:
        start = stack[-1]
        if graph.get(start):
            end = graph[start][0]
            stack.append(end)
            graph[start].remove(end)
        else:
            path.append(stack.pop())

    num_edges = sum((len(v) for v in graph.values()))
    if num_edges == 0:
        return list(reversed(path))
    return []


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


def StringReconstruction(patterns):
    adj_list = DeBruijnFromKmers(patterns)
    path = EulerianPath(adj_list)
    text = PathToGenome(path)
    return text


print(StringReconstruction(patterns))
file = open(
    "C:/Users/18687/Desktop/Bio Informatics/Bioinformatics specialization/stringreconstructionanswer.txt", "w")
file.write(StringReconstruction(patterns))

file.close()

if __name__ == "__main__":
    StringReconstruction(patterns)
