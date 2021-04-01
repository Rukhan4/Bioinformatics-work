"""
Code Challenge: Implement the nearest neighbor interchange heuristic for the Large Parsimony Problem.
Input: An integer n, followed by an adjacency list for an unrooted binary tree whose n leaves are labeled by DNA strings and
     whose internal nodes are labeled by integers.
Output: The parsimony score and unrooted labeled tree obtained after every step of the nearest neighbor interchange heuristic.
     Each step should be separated by a blank line.

The nearest neighbor interchange heuristic for the Large Parsimony Problem starts from an arbitrary unrooted binary tree. It assigns input strings to arbitrary leaves of this tree, assigns strings to the internal nodes of the tree by solving the Small Parsimony Problem in an Unrooted Tree, and then moves to a nearest neighbor that provides the best improvement in the parsimony score. At each iteration, the algorithm explores all internal edges of a tree and generates all nearest neighbor interchanges for each internal edge. For each of these nearest neighbors, the algorithm solves the Small Parsimony Problem to reconstruct the labels of the internal nodes and computes the parsimony score. If a nearest neighbor with smaller parsimony score is found, then the algorithm selects the one with smallest parsimony score (ties are broken arbitrarily) and iterates again; otherwise, the algorithm terminates. This is achieved by the following pseudocode.
"""
from small_parsimony_unrooted import small_parsimony_unrooted
from nearest_neighbor_tree import nearest_neighbor_tree
from small_parsimony import hamming_distance


def graph_to_string(tree_graph, node_character, leafs):
    list_tree = []
    for node_index, down_node_indexs in tree_graph.items():
        if node_index in leafs:
            node = node_character[node_index]
        else:
            node = str(node_index)
        for down_node_index in down_node_indexs:
            if down_node_index in leafs:
                down_node = node_character[down_node_index]
            else:
                down_node = str(down_node_index)
            list_tree.append(node + '->' + down_node)
    return('\n'.join(list_tree))


def nearest_neighbor_interchange(tree, n_leaf):
    score = float('Inf')
    tree, node_character, new_score = small_parsimony_unrooted(tree, n_leaf)
    leafs = list(range(n_leaf))
    internal_nodes = list(range(n_leaf, max(tree.keys()) + 1))
    new_tree = tree
    new_char = node_character
    #graph_to_string(tree, node_character, leafs)
    while new_score < score:

        score = new_score
        tree = new_tree
        node_character = new_char
        for internal_node in internal_nodes:
            down_nodes = tree[internal_node]
            for down_node in down_nodes:
                if down_node in internal_nodes:

                    neighbor_1, neighbor_2 = nearest_neighbor_tree(
                        internal_node, down_node, graph_to_string(tree, node_character, leafs))
                    neighbor_1_str = graph_to_string(neighbor_1, node_character, leafs)
                    neighbor_2_str = graph_to_string(neighbor_2, node_character, leafs)
                    tree1, node_character1, neighbor_score1 = small_parsimony_unrooted(
                        neighbor_1_str, n_leaf)
                    tree2, node_character2, neighbor_score2 = small_parsimony_unrooted(
                        neighbor_2_str, n_leaf)

                    if neighbor_score1 < new_score:
                        new_score = neighbor_score1
                        new_tree = tree1
                        new_char = node_character1
                    if neighbor_score2 < new_score:
                        new_score = neighbor_score2
                        new_tree = tree2
                        new_char = node_character2

        print(int(new_score))
        for node_index, down_node_indexs in new_tree.items():
            node = node_character[node_index]
            for down_node_index in down_node_indexs:
                down_node = node_character[down_node_index]
                print(str(node) + '->' + str(down_node) + ':' +
                      str(hamming_distance(node, down_node)))
        print('')


if __name__ == "__main__":

    #     n_leaf = 5
    #     tree = '''GCAGGGTA->5
    # TTTACGCG->5
    # CGACCTGA->6
    # GATTCCAC->6
    # 5->TTTACGCG
    # 5->GCAGGGTA
    # 5->7
    # TCCGTAGT->7
    # 7->5
    # 7->6
    # 7->TCCGTAGT
    # 6->GATTCCAC
    # 6->CGACCTGA
    # 6->7'''
    n_leaf = 8
    with open(r'C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\nearestneighborinterchange.txt', 'r') as input_file:
        tree = input_file.read()

    '''
    To run the script in ubuntu, provide absolute path by going to testset and using pwd
    with open("/mnt/c/Users/18687/Desktop/Bio Informatics/Bioinformatics specialization/testsets/nearestneighborinterchange.txt", 'r') as input_file:
    tree = input_file.read()
    '''

    print(nearest_neighbor_interchange(tree, n_leaf))
