"""
Burrows-Wheeler Transform Construction Problem: Construct the Burrows-Wheeler transform of a string.
Input: A string Text.
Output: BWT(Text).

Code Challenge: Solve the Burrows-Wheeler Transform Construction Problem.
"""


def BWT_construction(string):
    string_rotation = []
    BWT = ''

    for _ in range(len(string)):
        string = string[-1] + string[:-1]
        string_rotation.append(string)

    string_rotation.sort()

    for characters in string_rotation:
        BWT = BWT + characters[-1]

    return(BWT)


string = 'CGTTTGCTAT$'
print(BWT_construction(string))

# if __name__ == "__main__":
#     with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\BWT.txt", "r") as file:
#         string = file.read().strip()
#     print(BWT_construction(string))
