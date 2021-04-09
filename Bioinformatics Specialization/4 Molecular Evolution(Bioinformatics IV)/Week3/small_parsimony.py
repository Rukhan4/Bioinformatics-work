"""
Code Challenge: Implement SmallParsimony to solve the Small Parsimony Problem.
Input: An integer n followed by an adjacency list for a rooted binary tree with n leaves labeled by DNA strings.
Output: The minimum parsimony score of this tree, followed by the adjacency list of a tree corresponding to labeling
     internal nodes by DNA strings in order to minimize the parsimony score of the tree. 
"""
import numpy as np


def small_parsimony(tree, n_leaf):
    tree_graph = dict()
    tags = dict()
    n_character = 0
    current_node = 0
    node_character = dict()

    if type(tree) == str:
        tree = tree.split('\n')
        for line in tree:
            line = line.split('->')
            upper = int(line[0])

            # tag 1 for processed(have character), 0 for un-processed
            try:
                bottom = int(line[1])
                tags[bottom] = 0

                if upper in tree_graph:
                    tree_graph[upper].append(bottom)
                else:
                    tree_graph[upper] = [bottom]

            except:
                bottom = line[1]
                node_character[current_node] = bottom
                tags[current_node] = 1

                if upper in tree_graph:
                    tree_graph[upper].append(current_node)
                else:
                    tree_graph[upper] = [current_node]

                current_node = current_node + 1
                n_character = len(bottom)

    # find root
    for node in tree_graph.keys():
        if node not in tags:
            root = node
            break
    tags[root] = 0

    # make a matrix to record scores, character_score[node, character_index(ACGT), position of character].
    character_score = np.full((root + 1, 4, n_character), float('Inf'), float)

    # initalize the character_score matrix
    for node, tag in tags.items():
        if tag == 1:
            characters = node_character[node]
            for index in range(len(characters)):
                character = characters[index]
                character_index = 'ACGT'.index(character)
                character_score[node, character_index, index] = 0

    # fill the character_score matrix
    while 0 in tags.values():
        for node, tag in tags.items():
            if tag == 0:
                down_node_1, down_node_2 = tree_graph[node]
                if (tags[down_node_1] * tags[down_node_2]) == 1:
                    for position_index in range(n_character):
                        for character_index in range(4):
                            min_score = float('Inf')
                            for character_index_1 in range(4):
                                for character_index_2 in range(4):
                                    if character_index_1 == character_index:
                                        delta_1 = 0
                                    else:
                                        delta_1 = 1

                                    if character_index_2 == character_index:
                                        delta_2 = 0
                                    else:
                                        delta_2 = 1

                                    score = character_score[down_node_1, character_index_1, position_index] + \
                                        character_score[down_node_2, character_index_2,
                                                        position_index] + delta_1 + delta_2
                                    if score < min_score:
                                        min_score = score
                            character_score[node, character_index, position_index] = min_score
                    tags[node] = 1

    # find root characters
    root_character = ''
    for position_index in range(n_character):
        score_list = list(character_score[root, :, position_index])
        character_index = score_list.index(min(score_list))
        character = 'ACGT'[character_index]
        root_character = root_character + character
    node_character[root] = root_character

    # trackback to find all other characters
    while len(node_character) != root + 1:
        for node, down_nodes in tree_graph.items():
            if (node in node_character):
                if (down_nodes[0] not in node_character) & (down_nodes[1] not in node_character):
                    characters_1 = ''
                    characters_2 = ''

                    for position_index in range(n_character):
                        character = node_character[node][position_index]
                        character_index = 'ACGT'.index(character)
                        socre = character_score[node, character_index, position_index]

                        for character_index_1 in range(4):
                            for character_index_2 in range(4):
                                if character_index_1 == character_index:
                                    delta_1 = 0
                                else:
                                    delta_1 = 1

                                if character_index_2 == character_index:
                                    delta_2 = 0
                                else:
                                    delta_2 = 1

                                if socre == (character_score[down_nodes[0], character_index_1, position_index] + character_score[down_nodes[1], character_index_2, position_index] + delta_1 + delta_2):
                                    min_index_1, min_index_2 = character_index_1, character_index_2

                        character_1 = 'ACGT'[min_index_1]
                        character_2 = 'ACGT'[min_index_2]
                        characters_1 = characters_1 + character_1
                        characters_2 = characters_2 + character_2

                    node_character[down_nodes[0]] = characters_1
                    node_character[down_nodes[1]] = characters_2

                if (down_nodes[0] not in node_character) & (down_nodes[1] in node_character):
                    characters_1 = ''

                    for position_index in range(n_character):
                        character = node_character[node][position_index]
                        character_index = 'ACGT'.index(character)
                        socre = character_score[node, character_index, position_index]

                        character_2 = node_character[down_nodes[1]][position_index]
                        character_index_2 = 'ACGT'.index(character_2)

                        for character_index_1 in range(4):
                            if character_index_1 == character_index:
                                delta_1 = 0
                            else:
                                delta_1 = 1

                            if character_index_2 == character_index:
                                delta_2 = 0
                            else:
                                delta_2 = 1

                            if socre == (character_score[down_nodes[0], character_index_1, position_index] + character_score[down_nodes[1], character_index_2, position_index] + delta_1 + delta_2):
                                min_index_1 = character_index_1

                        character_1 = 'ACGT'[min_index_1]
                        characters_1 = characters_1 + character_1
                    node_character[down_nodes[0]] = characters_1

                if (down_nodes[0] in node_character) & (down_nodes[1] not in node_character):
                    characters_2 = ''

                    for position_index in range(n_character):
                        character = node_character[node][position_index]
                        character_index = 'ACGT'.index(character)
                        socre = character_score[node, character_index, position_index]

                        character_1 = node_character[down_nodes[0]][position_index]
                        character_index_1 = 'ACGT'.index(character_1)

                        for character_index_2 in range(4):
                            if character_index_1 == character_index:
                                delta_1 = 0
                            else:
                                delta_1 = 1

                            if character_index_2 == character_index:
                                delta_2 = 0
                            else:
                                delta_2 = 1

                            if socre == (character_score[down_nodes[0], character_index_1, position_index] + character_score[down_nodes[1], character_index_2, position_index] + delta_1 + delta_2):
                                min_index_2 = character_index_2

                        character_2 = 'ACGT'[min_index_2]
                        characters_2 = characters_2 + character_2
                    node_character[down_nodes[1]] = characters_2

    # connect node to each other
    new_graph = dict()
    for node, down_nodes in tree_graph.items():
        if down_nodes[0] not in tree_graph:
            new_graph[down_nodes[0]] = [node]
        else:
            if node not in tree_graph[down_nodes[0]]:
                tree_graph[down_nodes[0]].append(node)

        if down_nodes[1] not in tree_graph:
            new_graph[down_nodes[1]] = [node]
        else:
            if node not in tree_graph[down_nodes[1]]:
                tree_graph[down_nodes[1]].append(node)

    tree_graph = {**tree_graph, **new_graph}

    # calculate score for root
    final_score = 0
    for position_index in range(n_character):
        character = node_character[root][position_index]
        character_index = 'ACGT'.index(character)
        position_score = character_score[root, character_index, position_index]
        final_score = final_score + position_score

    return(tree_graph, node_character, final_score)


def hamming_distance(string1, string2):
    mismatch = 0
    for base1, base2 in zip(string1, string2):
        if base1 != base2:
            mismatch = mismatch + 1
    return (mismatch)


if __name__ == "__main__":

    #     n_leaf = 4
    #     tree = '''4->CAAATCCC
    # 4->ATTGCGAC
    # 5->CTGCGCTG
    # 5->ATGGACGA
    # 6->4
    # 6->5'''
    n_leaf = 128
    with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\smallparsimony.txt", "r") as input_file:
        tree = input_file.read()

    tree_graph, node_character, final_score = small_parsimony(tree, n_leaf)

    print(int(final_score))
    for node_index, down_node_indexs in tree_graph.items():
        node = node_character[node_index]
        for down_node_index in down_node_indexs:
            down_node = node_character[down_node_index]
            print(str(node) + '->' + str(down_node) + ':' + str(hamming_distance(node, down_node)))

    # cd to folder in terminal and run script there
