"""
Code Challenge: Solve the Nearest Neighbors of a Tree Problem.
Input: Two internal nodes a and b specifying an edge e, followed by an adjacency list of an unrooted binary tree.
Output: Two adjacency lists representing the nearest neighbors of the tree with respect to e. Separate the
     adjacency lists with a blank line.
"""

import copy


def nearest_neighbor_tree(a, b, tree):

    a = str(a)
    b = str(b)

    graph_tree = dict()
    if type(tree) == str:
        tree = tree.split('\n')
    for line in tree:
        line = line.split('->')
        if line[0] in graph_tree:
            graph_tree[line[0]].append(line[1])
        else:
            graph_tree[line[0]] = [line[1]]

    graph_tree[a].remove(b)
    graph_tree[b].remove(a)

    _, x = graph_tree[a]
    y, z = graph_tree[b]

    graph_tree[a].append(b)
    graph_tree[b].append(a)

    new_tree = copy.deepcopy(graph_tree)
    new_tree[a].remove(x)
    new_tree[x].remove(a)
    new_tree[b].remove(y)
    new_tree[y].remove(b)

    new_tree[a].append(y)
    new_tree[y].append(a)
    new_tree[b].append(x)
    new_tree[x].append(b)

    neighbor_tree = copy.deepcopy(graph_tree)
    neighbor_tree[a].remove(x)
    neighbor_tree[x].remove(a)
    neighbor_tree[b].remove(z)
    neighbor_tree[z].remove(b)

    neighbor_tree[a].append(z)
    neighbor_tree[z].append(a)
    neighbor_tree[b].append(x)
    neighbor_tree[x].append(b)

    return(new_tree, neighbor_tree)


if __name__ == "__main__":

    # a, b = 5, 4
    # tree = '''0->4
    # 4->0
    # 1->4
    # 4->1
    # 2->5
    # 5->2
    # 3->5
    # 5->3
    # 4->5
    # 5->4'''
    a, b = 34, 56
    with open(r'C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\nearestneighbortree.txt', 'r') as input_file:
        tree = input_file.read()

    new_tree, neighbor_tree = nearest_neighbor_tree(a, b, tree)

    for from_, tos in new_tree.items():
        for to in tos:
            print(str(from_) + '->' + str(to))
    print('')
    for from_, tos in neighbor_tree.items():
        for to in tos:
            print(str(from_) + '->' + str(to))
