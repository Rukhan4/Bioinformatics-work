# Implement GraphToGenome.

# Input: The colored edges ColoredEdges of a genome graph.
# Output: The genome P corresponding to this genome graph.

def graph_to_genome(genome_graph):

    if type(genome_graph) == str:
        genome_graph = genome_graph.replace('(', '').replace(')', '').replace(' ', '')
        genome_graph = genome_graph.split(',')
        genome_graph = list(map(int, genome_graph))

    else:
        tmp_genome_graph = []
        for sub_genome_graph in genome_graph:
            tmp_genome_graph.extend(sub_genome_graph)
        genome_graph = tmp_genome_graph

    p = []

    start_index = 0

    for i in range(start_index + 1, len(genome_graph)):
        if (i % 2 == 0) & (abs(genome_graph[i] - genome_graph[i - 1]) > 1):
            nodes = genome_graph[start_index: i]
            nodes = [nodes[-1]] + nodes[:-1]
            choromosome = cycle_to_chromosome(nodes)
            p.append(choromosome)
            start_index = i

    nodes = genome_graph[start_index:]
    nodes = [nodes[-1]] + nodes[:-1]
    choromosome = cycle_to_chromosome(nodes)
    p.append(choromosome)

    return(p)


def cycle_to_chromosome(nodes):
    if type(nodes) == str:
        nodes = nodes.split(' ')
    nodes = list(map(int, nodes))
    nodes = [0] + nodes

    chromosome = []

    for i in range(1, (int(len(nodes)/2) + 1)):
        if nodes[2 * i - 1] < nodes[2 * i]:
            node = int(nodes[2*i] / 2)
            #positive = '+'
            #node = f'{positive}{node}'
        else:
            node = int(-1 * nodes[(2*i) - 1] / 2)

        chromosome.append(node)

    return chromosome


if __name__ == "__main__":
    genome_graph = '(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)'
    print(tuple(graph_to_genome(genome_graph)))
