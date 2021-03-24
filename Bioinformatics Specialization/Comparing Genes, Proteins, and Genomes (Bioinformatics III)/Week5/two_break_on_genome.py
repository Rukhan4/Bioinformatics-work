# Implement 2-BreakOnGenome.
# Input: A genome P, followed by indices i1 , i2 , i3 , and i4 .
# Output: The genome P' resulting from applying the 2-break operation 2-BreakOnGenome(GenomeGraph i1 , i2 , i3 , i4 ).
import copy
from two_break_distance import two_break_distance
from two_break_on_genome_graph import two_break_on_genome_graph
from colored_edges import colored_edges
from graph_to_genome import graph_to_genome
from cycle_to_chromosome import cycle_to_chromosome
from chromosome_to_cycle import chromosome_to_cycle


def two_break_sort_graph(edges):
    tmp_edges = copy.deepcopy(edges)
    master_output_edges = []

    while len(tmp_edges) != 0:
        output_edges = [copy.deepcopy(tmp_edges[0])]
        tmp_edges.pop(0)

        while True:
            if (output_edges[0][0]) % 2 == 0:
                if (output_edges[0][0] - output_edges[-1][1]) == 1:
                    break
            if (output_edges[0][0]) % 2 == 1:
                if (output_edges[0][0] - output_edges[-1][1]) == -1:
                    break

            for edge in tmp_edges:

                last_number = output_edges[-1][1]
                if (last_number % 2) == 0:
                    if (last_number - 1) in edge:
                        if last_number - 1 == edge[0]:
                            output_edges.append(edge)
                        else:
                            output_edges.append(edge[::-1])
                        tmp_edges.remove(edge)

                else:
                    if (last_number + 1) in edge:
                        if last_number + 1 == edge[0]:
                            output_edges.append(edge)
                        else:
                            output_edges.append(edge[::-1])
                        tmp_edges.remove(edge)

        master_output_edges.extend(output_edges)

    return(master_output_edges)


def print_genome(P):
    output_print = ''
    tmp_P = copy.deepcopy(P)

    for sub_p in tmp_P:
        print_sub = '('

        for i in range(len(sub_p)):
            if sub_p[i] > 0:
                sub_p[i] = '+' + str(sub_p[i])
            else:
                sub_p[i] = str(sub_p[i])

            print_sub = print_sub + sub_p[i] + ' '

        print_sub = print_sub[: -1] + ')'
        output_print = output_print + print_sub

    print(output_print)


def shortest_rearrangement_scenario(P, Q):
    print(P)
    red_edges = colored_edges(P)
    blue_edges = colored_edges(Q)

    #red_blue_edges = red_edges + blue_edges

    while two_break_distance(P, Q) != 0:

        for blue_edge in blue_edges:
            if (blue_edge[::-1] not in red_edges) & (blue_edge not in red_edges):
                i1, i3 = blue_edge[0], blue_edge[1]
                for red_edge in red_edges:
                    if red_edge[0] == i1:
                        i2 = red_edge[1]
                    elif red_edge[1] == i1:
                        i2 = red_edge[0]

                    if red_edge[0] == i3:
                        i4 = red_edge[1]
                    elif red_edge[1] == i3:
                        i4 = red_edge[0]

                red_edges = two_break_on_genome_graph(red_edges, i1, i2, i3, i4)
                red_edges = two_break_sort_graph(red_edges)
                P = graph_to_genome(red_edges)
                print_genome(P)

                break


# P = "(+1 +2 +3 +4)(+5 +6)(+7 +8 +9)"
# Q = "(+1 +2 +3 +4)(+5 -9 -8 -7 +6)"
# print(shortest_rearrangement_scenario(P, Q))


if __name__ == "__main__":
    with open(r'C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\2breaksorting.txt', 'r') as input_file:
        P = input_file.readline().strip()
        Q = input_file.readline().strip()

    shortest_rearrangement_scenario(P, Q)
