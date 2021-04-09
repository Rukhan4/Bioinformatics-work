""" 
Code Challenge: Solve the Trie Construction Problem.

Input: A collection of strings Patterns.
Output: The adjacency list corresponding to Trie(Patterns), in the following format. If Trie(Patterns) has n nodes, 
first label the root with 0 and then label the remaining nodes with the integers 1 through n - 1 in any order you like. 
Each edge of the adjacency list of Trie(Patterns) will be encoded by a triple: 
the first two members of the triple must be the integers labeling the initial and terminal nodes of the edge, respectively; 
the third member of the triple must be the symbol labeling the edge.
"""


def trie_construction(strings):
    if type(strings) == str:
        strings = strings.split('\n')

    added_strings = dict()
    trie = dict()

    # add the first string in to trie
    string = strings[0]
    for position in range(len(string)):
        base = string[position]
        trie[position] = {position + 1: base}
        max_label = position + 2
    added_strings[strings[0]] = len(strings[0]) - 1

    for string in strings[1:]:
        label_delta = 0
        start_position = 0
        jump_position = 0

        # find the longest prefix of string which already in trie
        max_len = 0
        prefix_string = ''
        for added_string in added_strings.keys():
            for i in range(1, len(added_string) + 1):
                s = added_string[:i]
                if s == string[:len(s)]:
                    if i > max_len:
                        max_len = i
                        prefix_string = s

        current_node = 0
        if prefix_string != '':
            for i in range(len(prefix_string)):
                for node, base in trie[current_node].items():
                    if base == prefix_string[i]:
                        current_node = node
                        jump_position = node
                        break

        # start to add the base which do not exist in trie
        start_position = len(prefix_string)

        # jump_position is to control if the new string have any prefix in trie
        # label_delta is to contral the new node label

        for position in range(start_position, len(string)):
            base = string[position]
            label = position + label_delta + jump_position - start_position

            if label in trie:

                if (label + 1) in trie[label]:

                    if trie[label][label + 1] == base:
                        continue

                    else:
                        trie[label][max_label] = base
                        if (max_label - label != 1):
                            label_delta = max_label - label - 1
                        max_label = max_label + 1
                        if position == len(string) - 1:
                            added_strings[string] = position + label_delta + \
                                jump_position - start_position + 1
                else:
                    trie[label] = {max_label: base}
                    if (max_label - label != 1):
                        label_delta = max_label - label - 1
                    max_label = max_label + 1
                    if position == len(string) - 1:
                        added_strings[string] = position + label_delta + \
                            jump_position - start_position + 1
            else:
                trie[label] = {max_label: base}
                if (max_label - label != 1):
                    label_delta = max_label - label - 1
                max_label = max_label + 1
                if position == len(string) - 1:
                    added_strings[string] = position + label_delta + \
                        jump_position - start_position + 1

    return(trie)


# strings = '''ATAGA
# ATC
# GAT'''

# print(trie_construction(strings))

if __name__ == "__main__":
    with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\trieconstruction.txt", "r") as file:
        strings = file.read()
    graph = trie_construction(strings)

    with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\trieconstructionanswer.txt", "w") as output_file:
        for key1, values1 in graph.items():
            for key2, value2 in values1.items():
                #print(str(key1) + '->' + str(key2) + ':' + value2)
                output_file.write(str(key1) + '->' + str(key2) + ':' + value2)
