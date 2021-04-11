"""
Suffix Array Construction Problem: Construct the suffix array of a string.

Input: A string Text.
Output: SuffixArray(Text).
"""


def suffix_array_construction(text):
    char_indexs = []
    index = []
    for i in range(len(text)):
        char_indexs.append([text[i:], i])

    char_indexs.sort()

    for char_index in char_indexs:
        index.append(char_index[1])

    return index


text = "cocoon$"
res = suffix_array_construction(text)
print(", ".join(map(str, res)))

# if __name__ == "__main__":
#     with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\suffixarrayconstruction.txt", "r") as file:
#         text = file.read().strip()
#     res = suffix_array_construction(text)
#     print(", ".join(map(str, res)))
