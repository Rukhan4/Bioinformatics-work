def maximal_nonbranching_path(graph):
    paths = []

    in_count, out_count = count_in_out(graph)

    for node in in_count.keys():
        if (in_count.get(node) != 1) | (out_count.get(node) != 1):
            if out_count[node] > 0:
                for n, base in graph[node].items():
                    non_branching_path = base[0]
                    next_node = n

                    while (in_count[next_node] == out_count[next_node] == 1):
                        non_branching_path = non_branching_path + \
                            list(graph[next_node].values())[0][0]
                        next_node = list(graph[next_node].keys())[0]
                    paths.append(non_branching_path)
    return(paths)


def count_in_out(graph):
    in_count = {}
    out_count = {}

    for key_1, values_1 in graph.items():
        out_count[key_1] = len(values_1)

        for key_2, values_2 in values_1.items():
            in_count[key_2] = 1

    in_count[0] = 0
    for key in in_count.keys():
        if key not in out_count:
            out_count[key] = 0

    return(in_count, out_count)
