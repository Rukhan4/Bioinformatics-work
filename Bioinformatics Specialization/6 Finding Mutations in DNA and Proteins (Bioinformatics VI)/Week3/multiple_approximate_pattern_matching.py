""" 
Code Challenge: Solve the Multiple Approximate Pattern Matching Problem.

Input: A string Text, followed by a collection of strings Patterns, and an integer d.
Output: All positions where one of the strings in Patterns appears as a substring of Text with at most d mismatches.
"""
import copy
from multiple_pattern_matching import inverse_BWT_number, BWT_construction


def BW_Matching_d_Mismatch(string, patterns, d):

    if type(patterns) == str:
        patterns = patterns.split(' ')

    string = string + '$'
    BWT_string = BWT_construction(string)

    inverse_BWT_list = inverse_BWT_number(BWT_string)

    last_col = list(BWT_string)
    first_col = copy.deepcopy(last_col)
    first_col.sort()

    inverse_BWT_list = inverse_BWT_number(BWT_string)

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

    positions = []

    for pattern in patterns:

        candidate_first_col = list(range(len(first_col)))

        n_mistake = {}

        for candidate in candidate_first_col:
            n_mistake[candidate] = 0

        while True:

            if len(pattern) > 1:

                symbol = pattern[-1]
                pattern = pattern[:-1]

                next_candidate_first_col = []
                next_n_mistake = {}

                for index in candidate_first_col:

                    current_symbol = first_col[index][0]

                    if current_symbol == symbol:
                        next_index = first_col.index(last_col[index])
                        next_candidate_first_col.append(next_index)
                        next_n_mistake[next_index] = int(n_mistake[index])

                    else:

                        n_mistake[index] = n_mistake[index] + 1
                        if n_mistake[index] <= d:
                            next_index = first_col.index(last_col[index])
                            next_candidate_first_col.append(next_index)
                            next_n_mistake[next_index] = int(n_mistake[index])

                candidate_first_col = next_candidate_first_col
                n_mistake = next_n_mistake

            elif len(pattern) == 1:
                candidate_first_col = next_candidate_first_col
                n_mistake = next_n_mistake

                symbol = pattern[-1]
                pattern = pattern[:-1]

                next_candidate_first_col = []
                next_n_mistake = {}

                for index in candidate_first_col:

                    current_symbol = first_col[index][0]

                    if current_symbol == symbol:

                        next_candidate_first_col.append(index)
                        next_n_mistake[next_index] = int(n_mistake[index])

                    else:

                        n_mistake[index] = n_mistake[index] + 1
                        if n_mistake[index] <= d:

                            next_candidate_first_col.append(index)
                            next_n_mistake[next_index] = int(n_mistake[index])

            else:

                for i in next_candidate_first_col:

                    position = inverse_BWT_list.index(first_col[i])
                    positions.append(position)

                break

    return(positions)


# string = 'ACATGCTACTTT'
# patterns = 'ATT GCC GCTA TATT'
# d = 1

# print(*BW_Matching_d_Mismatch(string, patterns, d))

if __name__ == "__main__":
    with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\multipleapproxpatternmatching.txt", "r") as file:
        string = file.readline().strip()
        #d = int(file.readline().strip())
        d = 2
        listans = []
        for line in file:
            listans.append(line.strip())
        patterns = ' '.join(listans)

    print(*BW_Matching_d_Mismatch(string, patterns, d))
