"""
Code Challenge: Solve the Suffix Tree Construction Problem.

Input: A string Text.
Output: The edge labels of SuffixTree(Text). You may return these strings in any order.
"""
from maximal_nonbranching_path import maximal_nonbranching_path, count_in_out


def suffix_tree_construction(text):
    trie = {}
    positions = {}
    new_node = 1

    for i in range(len(text)):
        current_node = 0
        for j in range(i, len(text)):
            current_symbol = text[j]

            check = 0
            if current_node in trie:
                for node, symbol_position in trie[current_node].items():
                    if symbol_position[0] == current_symbol:
                        current_node = node
                        check = 1
                        break
            if check == 0:
                if current_node in trie:
                    trie[current_node][new_node] = [current_symbol, j]
                    # current_node = new_node
                    # new_node     = new_node + 1
                else:
                    trie[current_node] = {new_node: [current_symbol, j]}
                current_node = new_node
                new_node = new_node + 1

        if current_node not in trie:
            positions[current_node] = i

    return(trie, positions)


if __name__ == "__main__":
    text = 'ATATCGTTTTATCGTT$'

    graph, positions = suffix_tree_construction(text)
    for edge in maximal_nonbranching_path(graph):
        print(edge)
