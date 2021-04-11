'''
Code Challenge: Solve the Multiple Pattern Matching Problem.
Input: A string Text followed by a collection of strings Patterns.
Output: All starting positions in Text where a string from Patterns appears as a substring.
'''
import copy


def inverse_BWT_number(BWT_string):

    BWT_string = list(BWT_string)
    first_col = copy.deepcopy(BWT_string)
    first_col.sort()

    inverse_BWT_list = []

    for base in "ACGT":
        count = 0
        for index in range(len(BWT_string)):
            if BWT_string[index] == base:
                BWT_string[index] = base + str(count)
                count = count + 1

    for base in "ACGT":
        count = 0
        for index in range(len(first_col)):
            if first_col[index] == base:
                first_col[index] = base + str(count)
                count = count + 1

    char = '$'
    inverse_BWT_list.append(char)

    while len(inverse_BWT_list) != len(BWT_string):
        index = BWT_string.index(char)
        char = first_col[index]
        inverse_BWT_list.append(char)

    inverse_BWT_list = inverse_BWT_list[1:] + list(inverse_BWT_list[0])

    return(inverse_BWT_list)


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


def BW_multiple_pattern_matching(string, patterns):

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

                    break

                else:
                    top = first_col.index(last_col[top_index])
                    bottom = first_col.index(last_col[bottom_index])
            else:

                for i in range(top, bottom + 1):

                    position = inverse_BWT_list.index(first_col[i])
                    positions.append(position)

                break

    return(positions)


# string = 'AATCGGGTTCAATCGGGGT'
# patterns = 'ATCG GGGT'

# print(*BW_multiple_pattern_matching(string, patterns))


if __name__ == "__main__":
    with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\multiplepatternmatching.txt", "r") as file:
        string = file.readline().strip()
        listans = []
        for line in file:
            listans.append(line.strip())
        patterns = ' '.join(listans)

    print(*BW_multiple_pattern_matching(string, patterns))
