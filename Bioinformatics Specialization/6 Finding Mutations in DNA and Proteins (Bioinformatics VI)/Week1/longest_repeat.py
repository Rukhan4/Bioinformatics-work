""" 
Longest Repeat Problem: Find the longest repeat in a string.
Input: A string Text.
Output: A longest substring of Text that appears in Text more than once.

Code Challenge: Solve the Longest Repeat Problem. (Multiple solutions may exist, in which case you may return any one.)
"""

import copy
from maximal_nonbranching_path import count_in_out


def Longest_Repeat_in_String(string):
    trie = Modified_Suffix_Trie_Construction(string + '$')

    end_nodes = []
    backward_graph = {}
    repeat_strings = []

    # find all the node have at least two sub-node, and make a backward graph for them
    for key_1, value_1 in trie.items():
        for key_2, value_2 in value_1.items():
            if key_2 in trie:
                if len(trie[key_2]) > 1:
                    end_nodes.append(key_2)
                    backward_graph[key_2] = [key_1, value_2[0]]

    # backtrack
    for node in backward_graph.keys():
        repeat_string = ''
        while node != 0:
            repeat_string = backward_graph[node][1] + repeat_string
            node = backward_graph[node][0]
            repeat_strings.append(repeat_string)

    # find the longest repeat string
    max_len = -1
    for string in repeat_strings:
        string_len = len(string)
        if string_len > max_len:
            max_len = string_len
            longest_string = string

    return(longest_string)


def Modified_Suffix_Trie_Construction(text):
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

                else:
                    trie[current_node] = {new_node: [current_symbol, j]}
                current_node = new_node
                new_node = new_node + 1

        if current_node not in trie:
            positions[current_node] = i

    paths = []

    in_count, out_count = count_in_out(trie)

    for node in in_count.keys():
        if (in_count.get(node) != 1) | (out_count.get(node) != 1):
            if out_count[node] > 0:

                for n, base in trie[node].items():
                    non_branching_path = base[0]
                    next_node = n

                    while (in_count[next_node] == out_count[next_node] == 1):
                        non_branching_path = non_branching_path + \
                            list(trie[next_node].values())[0][0]
                        next_node_tmp = list(trie[next_node].keys())[0]
                        length = list(trie[next_node].values())[0][1]
                        trie.pop(next_node)
                        next_node = next_node_tmp

                    if n != next_node:
                        if n in trie:
                            trie[n][next_node] = [non_branching_path, base[1], length + 1 - base[1]]
                        else:
                            trie[n] = {next_node: [non_branching_path,
                                                   base[1], length + 1 - base[1]]}

                    paths.append(non_branching_path)

    tmp_trie = {}

    for node_1, key_1 in trie.items():
        if len(key_1) != 1:
            tmp_trie[node_1] = copy.deepcopy(key_1)

    for node_1, key_1 in tmp_trie.items():
        for node_2, key_2 in key_1.items():

            if node_2 in trie:
                if len(trie[node_2]) == 1:
                    trie[node_1].pop(node_2)
                    trie[node_1][list(trie[node_2].keys())[0]] = list(trie[node_2].values())[0]
                    trie.pop(node_2)

    return(trie)


if __name__ == "__main__":

    string = '''ACGTGTTGCATGCGCGATTAAGTGCCCGTAATGCGGCCGGTAATAGTCCTTCAAAAGGACCCTTGATAAGGAAATAAGTGTACAATCATATACCTCCGAGGAGTTGCGGCGGACGAGTAATTTAGCGGTGCGAGCCCCAGTCTGGATAATAGCAACAAGACGTCAGCCGCTCTGCCAAATAAAGCCCCGGGAAATCAGTCCGCCTTCTTGGTGGATCGTGCCCAGATACCACTCCTTTGAGGAGCAGAGATATGTAGAGGAACACAGAACTTTGATTTTTGTATAGTGGGAGGATGTATCGTAATGCACTCGACGATTATGCCTGTAGGTGCTCGGCTAGGCAGCAAAGACCCCCCTTTAACACGTTGACATGCAACATGCTAATCAGAGTCGGACAACGGGCATTACGGCCATTGCACTGCCATCTGTATAAGCGTGGCAGAATCTTAGCGGCATCCAAAACTCTGCCTATGCCCGGTGGAGGTAATACGTAACTGACCGTGATCAGTGGTAAATACGCCGTTATTGGTTCAAGCTTGGTATTCGGCCCATGTGTGAAGATCACGGTTATATGAACCAATAGGATACCTTGATATCTCTAGATCGCGGAGTGGACTAGAATTTAGCTATTCAAGAGTAGTACAGTCGTTAGCCCCCACGGCCTTACATCCAAATTTGCTGCGAGAGGGTTTGGCTCTTTCGGGAAATGACTTGTTCTGGTTGCTATAAGGTCGCTATAACCTTACGATCGTACACCCCTCTGTACACTAGCCCACGTAAGCTGCGATCTGATTCGCCCTAAGTTCGAGCGCTATTGCGTTCCCCCTATCGAGTTATATTACGAACGCGCCGCGCCCCATGTGGTGACAGTTGCGCCTCCGATCAACTTTCACCACTCCTTTGAGGAGCAGAGATATGTAGAGGAACACAGAACTTTGATTTTTGTATAGTGGGAGGATGTATCGTAATGCACTCGACGCGCTGCCGGTGTTGACCACTCCTTTGAGGAGCAGAGATATGTAGAGGAACACAGAACTTTGATTTTTGTATAGTGGGAGGATGTATCGTAATGCACTCGAATGTCAGCGAGCTTTTGGACGGGTGTGTTGAGCCAGTCACTGACGGGCTGTAGAAGCGATACATAGGTCGACGTGGGTCACGTACATGGAAAGTCAGTTAGGGATGTAATCTGTGGCCCGCTGAGAGCCTCGTGCTTGTTCGCCTTTCTTAACCTGTCTATACACGCTCTGTGGAGAAT'''

    print(Longest_Repeat_in_String(string))
