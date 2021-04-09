'''
Longest Shared Substring Problem: Find the longest substring shared by two strings.
Input: Strings Text1 and Text2.
Output: The longest substring that occurs in both Text1 and Text2.

Code Challenge: Solve the Longest Shared Substring Problem. (Multiple solutions may exist, in which case you may return any one.)
'''
from maximal_nonbranching_path import count_in_out
from longest_repeat import Modified_Suffix_Trie_Construction


def Longest_Shared_Substring(string_1, string_2):
    text = string_1 + '#' + string_2 + '$'
    trie = Modified_Suffix_Trie_Construction(text)
    in_count, _ = count_in_out(trie)
    classification = {}  # 1 for string_1, 2 for string_2, 3 for both

    # classify each node from leaf
    while len(in_count) != len(classification):
        for key_1, value_1 in trie.items():
            if key_1 not in classification:
                nodes_class = []
                for key_2, value_2 in value_1.items():
                    if '$' in value_2[0]:
                        if '#' in value_2[0]:
                            classification[key_2] = 1
                        else:
                            classification[key_2] = 2
                    nodes_class.append(classification.get(key_2, -1))
                if -1 not in nodes_class:
                    if 3 in nodes_class:
                        classification[key_1] = 3

                    elif (1 in nodes_class) & (2 in nodes_class):
                        classification[key_1] = 3

                    else:
                        classification[key_1] = nodes_class[0]

    # make a backward graph for shared_edge, which if good to construct shared path
    shared_edge_back = {}
    for key_1, values_1 in trie.items():
        if classification[key_1] == 3:
            for key_2, values_2 in values_1.items():
                if classification[key_2] == 3:
                    shared_edge_back[key_2] = [key_1, values_2[0]]

    # find all shared path
    shared_paths = []
    for key in shared_edge_back.keys():
        shared_path = ''
        node = key
        while node != 0:
            pattern = shared_edge_back[node][1]
            shared_path = pattern + shared_path
            node = shared_edge_back[node][0]

        shared_paths.append(shared_path)

    # find the longest shared path
    max_len = -1
    for string in shared_paths:
        string_len = len(string)
        if string_len > max_len:
            max_len = string_len
            longest_string = string

    return(longest_string)


# string_1 = 'TCGGTAGATTGCGCCCACTC'
# string_2 = 'AGGGGCTCGCAGTGTAAGAA'

# print(Longest_Shared_Substring(string_1, string_2))

if __name__ == "__main__":
    with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\longestsharedsubstring.txt", "r") as file:
        string_1 = file.readline().strip()
        string_2 = file.readline()
    print(Longest_Shared_Substring(string_1, string_2))
