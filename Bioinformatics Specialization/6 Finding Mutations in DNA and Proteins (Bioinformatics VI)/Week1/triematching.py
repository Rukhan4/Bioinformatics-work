""" 
Code Challenge: Implement TrieMatching to solve the Multiple Pattern Matching Problem.

Input: A string Text and a collection of strings Patterns.
Output: All starting positions in Text where a string from Patterns appears as a substring.
"""
from trie_construction import trie_construction


def prefix_tree_matching(text, trie):
    node = 0
    index = 0

    while index != len(text):
        base = text[index]
        if node in trie:
            check = 0
            for n, b in trie[node].items():
                if b == base:
                    node = n
                    index = index + 1
                    check = 1
                    break
            if check == 0:
                return(0)
        else:
            return(1)

    return(1)


def trie_matching(text, patterns):
    if type(patterns) == str:
        trie = trie_construction(patterns)

    positions = []
    for i in range(len(text) - 1):
        check = prefix_tree_matching(text[i:], trie)
        if check == 1:
            positions.append(i)

    return(positions)


# text = 'AATCGGGTTCAATCGGGGT'
# patterns = '''ATCG
# GGGT'''

# print(*trie_matching(text, patterns))

if __name__ == "__main__":
    with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\triematching.txt", "r") as file:
        text = file.readline().strip()
        patterns = file.read().strip()
        print(*trie_matching(text, patterns))
