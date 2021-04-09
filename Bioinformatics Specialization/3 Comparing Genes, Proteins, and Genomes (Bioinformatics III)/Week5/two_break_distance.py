# Solve the 2-Break Distance Problem.

# Input: Genomes P and Q.
# Output: The 2-break distance d(P, Q).


def two_break_distance(P, Q):
    p = colored_edges(P)
    q = colored_edges(Q)

    comb = p + q

    n_cycle = 0
    while len(comb) != 0:
        n_cycle = n_cycle + 1
        current_cycle = comb[0]
        comb.pop(0)
        for number in current_cycle:
            for edge in comb:
                if number in edge:
                    edge.remove(number)
                    current_cycle.extend(edge)
                    comb.remove(edge)

    return(len(q) - n_cycle)


def colored_edges(p):
    if type(p) == str:
        p = p[1:-1]
        p = p.split(')(')

    edges = []

    for chromosome in p:
        if type(chromosome) == str:
            chromosome = chromosome.split(' ')
            chromosome = list(map(int, chromosome))

        nodes = chromosome_to_cycle(chromosome)
        for i in range(1, int(len(chromosome))):
            edge = [nodes[2 * i - 1], nodes[2 * i]]
            edges.append(edge)
        last_edge = [nodes[-1], nodes[0]]
        edges.append(last_edge)

    return edges


def chromosome_to_cycle(chromosome):
    if type(chromosome) == str:
        chromosome = chromosome.split(' ')
    chromosome = list(map(int, chromosome))

    nodes = []
    for old_node in chromosome:
        if old_node > 0:
            nodes.extend([2 * old_node - 1, 2 * old_node])
        else:
            nodes.extend([-2 * old_node, -2 * old_node - 1])
    return nodes

#P = '(+1 +2 +3 +4 +5 +6)'
#Q = '(+1 -3 -6 -5)(+2 -4)'


if __name__ == "__main__":
    with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\2break.txt", 'r') as input_data:
        P, Q = [line.strip().lstrip('(').rstrip(')').split(')(') for line in input_data.readlines()]

    print(two_break_distance(P, Q))
