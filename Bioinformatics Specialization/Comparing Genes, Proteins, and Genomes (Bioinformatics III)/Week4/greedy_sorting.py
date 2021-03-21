# Greedy Sorting -
# Input: A permutation P.
# Output: The sequence of permutations corresponding to applying greedy_sorting to P,
# ending with the identity permutation.

def reverse(p_list):
    for i in range(len(p_list)):
        p_list[i] = p_list[i] * -1
    p_list = p_list[::-1]  # reversal
    return(p_list)


def print_p(p_list):
    p_list = list(map(str, p_list))
    p_list = p_list[1:]
    for i in range(len(p_list)):
        if (p_list[i][0]) != '-':
            p_list[i] = '+' + p_list[i]
    p_list = ' '.join(p_list)
    print(p_list)


def greedy_sorting(p):
    if type(p) == str:
        p = p.split(' ')
    p = list(map(int, p))
    distance = 0
    p = [0] + p

    for k in range(1, len(p)):
        while p[k] != k:
            print_p(p)  # Final line
            distance = distance + 1

            if p[k] == -k:
                p[k] = p[k] * -1

            elif (-k) in p:
                k_index = p.index(-k)
                p = p[: k] + reverse(p[k: k_index + 1]) + p[k_index + 1:]

            else:
                k_index = p.index(k)
                p = p[: k] + reverse(p[k: k_index + 1]) + p[k_index + 1:]
    print_p(p)
    return distance


with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\greedy_sorting.txt", "r") as inputfile:
    permutation = inputfile.read()

inputfile.close
greedy_sorting(permutation)

""" 
testp = "-3 +4 +1 +5 -2"
# testp2 = "+6 -12 -9 +17 +18 -4 +5 -3 +11 +19 +14 +10 +8 +15 -13 +20 +2 +7 -16 -1"
greedy_sorting(testp) """
