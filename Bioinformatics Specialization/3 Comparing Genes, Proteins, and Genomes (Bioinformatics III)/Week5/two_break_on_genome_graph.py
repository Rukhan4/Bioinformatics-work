# Implement 2-BreakOnGenomeGraph.

# Input: The colored edges of a genome graph GenomeGraph, followed by indices i1 , i2 , i3 , and i4 .
# Output: The colored edges of the genome graph resulting from applying the 2-break operation 2-BreakOnGenomeGraph(GenomeGraph, i1 , i2 , i3 , i4 ).
import copy


def two_break_on_genome_graph(genome_graph, i1, i2, i3, i4):
    if type(genome_graph) == str:
        genome_graph = genome_graph[1: -1]
        genome_graph = genome_graph.split('), (')
        for i in range(len(genome_graph)):
            genome_graph[i] = genome_graph[i].split(',')
            genome_graph[i] = list(map(int, genome_graph[i]))

    tmp_genome_graph = copy.deepcopy(genome_graph)
    for edge in genome_graph:

        if (i1 in edge) & (i2 in edge):
            tmp_genome_graph.remove(edge)

        elif (i3 in edge) & (i4 in edge):
            tmp_genome_graph.remove(edge)

    tmp_genome_graph.append((i1, i3))
    tmp_genome_graph.append((i2, i4))

    return(tmp_genome_graph)


if __name__ == "__main__":
    genome_graph = '(1, 3), (4, 6), (5, 7), (8, 10), (9, 11), (12, 13), (14, 15), (16, 17), (18, 19), (20, 21), (22, 23), (24, 26), (25, 28), (27, 30), (29, 32), (31, 33), (34, 35), (36, 38), (37, 39), (40, 42), (41, 44), (43, 45), (46, 48), (47, 50), (49, 52), (51, 53), (54, 56), (55, 58), (57, 60), (59, 62), (61, 64), (63, 66), (65, 68), (67, 70), (69, 72), (71, 73), (74, 76), (75, 77), (78, 80), (79, 81), (82, 84), (83, 85), (86, 87), (88, 89), (90, 92), (91, 94), (93, 95), (96, 98), (97, 99), (100, 101), (102, 103), (104, 106), (105, 107), (108, 110), (109, 112), (111, 114), (113, 115), (116, 118), (117, 120), (119, 121), (122, 124), (123, 126), (125, 127), (128, 129), (130, 131), (132, 134), (133, 135), (136, 138), (137, 2)'
    i1, i2, i3, i4 = 59, 62, 83, 85

    print(tuple(two_break_on_genome_graph(genome_graph, i1, i2, i3, i4)))
