#  Given two strings, find all their shared k-mers.

# Input: An integer k and two strings.
# Output: All k-mers shared by these strings, in the form of ordered pairs (x, y) corresponding to starting positions
# of these k-mers in the respective strings.

def reverse_compliment(DNA_string):
    complementry_rule = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    com_string = ''
    for base in DNA_string:
        com_string = com_string + complementry_rule[base]

    com_string = com_string[::-1]

    return (com_string)


def shared_kmers(string1, string2, k):
    kmers_position_1 = dict()
    kmers_position_2 = dict()
    shared_positions = []

    for start in range(len(string1) - k + 1):
        end = start + k
        pattern = string1[start: end]
        if pattern in kmers_position_1:
            kmers_position_1[pattern].append(start)
        else:
            kmers_position_1[pattern] = [start]

    for start in range(len(string2) - k + 1):
        end = start + k
        pattern = string2[start: end]
        if pattern in kmers_position_2:
            kmers_position_2[pattern].append(start)
        else:
            kmers_position_2[pattern] = [start]

    for pattern, positions in kmers_position_1.items():

        if pattern in kmers_position_2:

            for position_1 in positions:
                for position_2 in kmers_position_2[pattern]:
                    shared_positions.append([position_1, position_2])

        if reverse_compliment(pattern) in kmers_position_2:

            for position_1 in positions:
                for position_2 in kmers_position_2[reverse_compliment(pattern)]:
                    shared_positions.append([position_1, position_2])

    return(shared_positions)


# string1 = 'AAACTCATC'
# string2 = 'TTTCAAATC'
# k = 3
# print(shared_kmers(string1, string2, k))
# print(len(shared_kmers(string1,string2,k)))

if __name__ == "__main__":
    k = 15
    strings = []
    with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\sharedkmers.txt", 'r') as input_file:
        for line in input_file:
            strings.append(line.strip())

    string1, string2 = strings[0], strings[1]

    list_of_tuples = [tuple(x) for x in shared_kmers(string1, string2, k)]

    for kmers in sorted(list_of_tuples):
        print(kmers)

    print(len(list_of_tuples))
