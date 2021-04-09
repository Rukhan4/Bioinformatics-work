
'''
Shortest Non-Shared Substring Problem: Find the shortest substring of one string that does not appear in another string.
Input: Strings Text1 and Text2.
Output: The shortest substring of Text1 that does not appear in Text2.

Code Challenge: Solve the Shortest Non-Shared Substring Problem. (Multiple solutions may exist, in which case you may return any one.)
'''
from suffix_tree_construction import suffix_tree_construction
import copy


def shortest_non_shared_substring(string_1, string_2):
    trie = suffix_tree_construction(string_2)[0]
    min_len = float('Inf')

    for i in range(len(string_1)):
        string = string_1[i:]
        tmp_string = copy.deepcopy(string)

        node = 0
        length = 0
        check = 1

        while (node in trie) & (check == 1):
            check = 0

            for key, value in trie[node].items():

                if len(tmp_string) > 0:

                    if value[0] == tmp_string[0]:
                        length = length + 1
                        node = key
                        tmp_string = tmp_string[1:]
                        check = 1

        if len(string) > length:
            if length < min_len:
                min_len = length
                non_shared_string = string[: length + 1]

    return(non_shared_string)


# Test
# string_1 = 'CCAAGCTGCTAGAGG'
# string_2 = 'CATGCTGGGCTGGCT'

# print(shortest_non_shared_substring(string_1, string_2))

if __name__ == "__main__":
    with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\shortestnonsharedsubstring.txt", "r") as file:
        string_1 = file.readline().strip()
        string_2 = file.readline()
    print(shortest_non_shared_substring(string_1, string_2))
