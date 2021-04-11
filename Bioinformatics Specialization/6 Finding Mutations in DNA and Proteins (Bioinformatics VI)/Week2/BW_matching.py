'''
Code Challenge: Implement BWMatching.
Input: A string BWT(Text), followed by a collection of Patterns.
Output: A list of integers, where the i-th integer corresponds to the number of substring matches of the i-th member of Patterns in Text.
'''
import copy


def BW_Matching(BWT_string, patterns):

    if type(patterns) == str:
        patterns = patterns.split(' ')

    last_col = list(BWT_string)
    first_col = copy.deepcopy(last_col)
    first_col.sort()

    for base in "ACGT":
        count = 0
        for index in range(len(last_col)):
            if last_col[index] == base:
                last_col[index] = base + str(count)
                count = count + 1

    for base in "ACGT":
        count = 0
        for index in range(len(first_col)):
            if first_col[index] == base:
                first_col[index] = base + str(count)
                count = count + 1

    n_matchs = []

    for pattern in patterns:

        top = 0
        bottom = len(last_col) - 1

        while True:

            if len(pattern) > 0:
                symbol = pattern[-1]
                pattern = pattern[:-1]

                top_index = float('Inf')
                for index in range(top, bottom + 1):
                    current_symbol = last_col[index][0]

                    if current_symbol == symbol:
                        if index < top_index:
                            top_index = index
                        bottom_index = index

                if top_index == float('Inf'):  # if there is no match
                    n_matchs.append(0)
                    break

                else:
                    top = first_col.index(last_col[top_index])
                    bottom = first_col.index(last_col[bottom_index])
            else:
                mathchs = bottom - top + 1
                n_matchs.append(mathchs)
                break

    return(n_matchs)


# BWT_string = 'TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC'
# patterns = 'CCT CAC GAG CAG ATC'
# print(*BW_Matching(BWT_string, patterns))

if __name__ == "__main__":
    with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\BWTmatching.txt", "r") as file:
        BWT_string = file.readline().strip()
        patterns = file.read().strip()
    print(*BW_Matching(BWT_string, patterns))
