# Alignment with affine gap problem -
# Input: Two amino acid strings v and w (each of length at most 100).

# Output: The maximum alignment score between v and w, followed by an alignment of
# v and w achieving this maximum score.

# Use the BLOSUM62 scoring matrix, a gap opening penalty of 11, and a gap extension penalty of 1.

import numpy as np

blosum62_matrix = {
    'A': {'A': '4', 'C': '0', 'D': '-2', 'E': '-1', 'F': '-2', 'G': '0', 'H': '-2', 'I': '-1', 'K': '-1', 'L': '-1',
          'M': '-1', 'N': '-2', 'P': '-1', 'Q': '-1', 'R': '-1', 'S': '1', 'T': '0', 'V': '0', 'W': '-3', 'Y': '-2'},
    'C': {'A': '0', 'C': '9', 'D': '-3', 'E': '-4', 'F': '-2', 'G': '-3', 'H': '-3', 'I': '-1', 'K': '-3', 'L': '-1',
          'M': '-1', 'N': '-3', 'P': '-3', 'Q': '-3', 'R': '-3', 'S': '-1', 'T': '-1', 'V': '-1', 'W': '-2', 'Y': '-2'},
    'D': {'A': '-2', 'C': '-3', 'D': '6', 'E': '2', 'F': '-3', 'G': '-1', 'H': '-1', 'I': '-3', 'K': '-1', 'L': '-4',
          'M': '-3', 'N': '1', 'P': '-1', 'Q': '0', 'R': '-2', 'S': '0', 'T': '-1', 'V': '-3', 'W': '-4', 'Y': '-3'},
    'E': {'A': '-1', 'C': '-4', 'D': '2', 'E': '5', 'F': '-3', 'G': '-2', 'H': '0', 'I': '-3', 'K': '1', 'L': '-3',
          'M': '-2', 'N': '0', 'P': '-1', 'Q': '2', 'R': '0', 'S': '0', 'T': '-1', 'V': '-2', 'W': '-3', 'Y': '-2'},
    'F': {'A': '-2', 'C': '-2', 'D': '-3', 'E': '-3', 'F': '6', 'G': '-3', 'H': '-1', 'I': '0', 'K': '-3', 'L': '0',
          'M': '0', 'N': '-3', 'P': '-4', 'Q': '-3', 'R': '-3', 'S': '-2', 'T': '-2', 'V': '-1', 'W': '1', 'Y': '3'},
    'G': {'A': '0', 'C': '-3', 'D': '-1', 'E': '-2', 'F': '-3', 'G': '6', 'H': '-2', 'I': '-4', 'K': '-2', 'L': '-4',
          'M': '-3', 'N': '0', 'P': '-2', 'Q': '-2', 'R': '-2', 'S': '0', 'T': '-2', 'V': '-3', 'W': '-2', 'Y': '-3'},
    'H': {'A': '-2', 'C': '-3', 'D': '-1', 'E': '0', 'F': '-1', 'G': '-2', 'H': '8', 'I': '-3', 'K': '-1', 'L': '-3',
          'M': '-2', 'N': '1', 'P': '-2', 'Q': '0', 'R': '0', 'S': '-1', 'T': '-2', 'V': '-3', 'W': '-2', 'Y': '2'},
    'I': {'A': '-1', 'C': '-1', 'D': '-3', 'E': '-3', 'F': '0', 'G': '-4', 'H': '-3', 'I': '4', 'K': '-3', 'L': '2',
          'M': '1', 'N': '-3', 'P': '-3', 'Q': '-3', 'R': '-3', 'S': '-2', 'T': '-1', 'V': '3', 'W': '-3', 'Y': '-1'},
    'K': {'A': '-1', 'C': '-3', 'D': '-1', 'E': '1', 'F': '-3', 'G': '-2', 'H': '-1', 'I': '-3', 'K': '5', 'L': '-2',
          'M': '-1', 'N': '0', 'P': '-1', 'Q': '1', 'R': '2', 'S': '0', 'T': '-1', 'V': '-2', 'W': '-3', 'Y': '-2'},
    'L': {'A': '-1', 'C': '-1', 'D': '-4', 'E': '-3', 'F': '0', 'G': '-4', 'H': '-3', 'I': '2', 'K': '-2', 'L': '4',
          'M': '2', 'N': '-3', 'P': '-3', 'Q': '-2', 'R': '-2', 'S': '-2', 'T': '-1', 'V': '1', 'W': '-2', 'Y': '-1'},
    'M': {'A': '-1', 'C': '-1', 'D': '-3', 'E': '-2', 'F': '0', 'G': '-3', 'H': '-2', 'I': '1', 'K': '-1', 'L': '2',
          'M': '5', 'N': '-2', 'P': '-2', 'Q': '0', 'R': '-1', 'S': '-1', 'T': '-1', 'V': '1', 'W': '-1', 'Y': '-1'},
    'N': {'A': '-2', 'C': '-3', 'D': '1', 'E': '0', 'F': '-3', 'G': '0', 'H': '1', 'I': '-3', 'K': '0', 'L': '-3',
          'M': '-2', 'N': '6', 'P': '-2', 'Q': '0', 'R': '0', 'S': '1', 'T': '0', 'V': '-3', 'W': '-4', 'Y': '-2'},
    'P': {'A': '-1', 'C': '-3', 'D': '-1', 'E': '-1', 'F': '-4', 'G': '-2', 'H': '-2', 'I': '-3', 'K': '-1', 'L': '-3',
          'M': '-2', 'N': '-2', 'P': '7', 'Q': '-1', 'R': '-2', 'S': '-1', 'T': '-1', 'V': '-2', 'W': '-4', 'Y': '-3'},
    'Q': {'A': '-1', 'C': '-3', 'D': '0', 'E': '2', 'F': '-3', 'G': '-2', 'H': '0', 'I': '-3', 'K': '1', 'L': '-2',
          'M': '0', 'N': '0', 'P': '-1', 'Q': '5', 'R': '1', 'S': '0', 'T': '-1', 'V': '-2', 'W': '-2', 'Y': '-1'},
    'R': {'A': '-1', 'C': '-3', 'D': '-2', 'E': '0', 'F': '-3', 'G': '-2', 'H': '0', 'I': '-3', 'K': '2', 'L': '-2',
          'M': '-1', 'N': '0', 'P': '-2', 'Q': '1', 'R': '5', 'S': '-1', 'T': '-1', 'V': '-3', 'W': '-3', 'Y': '-2'},
    'S': {'A': '1', 'C': '-1', 'D': '0', 'E': '0', 'F': '-2', 'G': '0', 'H': '-1', 'I': '-2', 'K': '0', 'L': '-2',
          'M': '-1', 'N': '1', 'P': '-1', 'Q': '0', 'R': '-1', 'S': '4', 'T': '1', 'V': '-2', 'W': '-3', 'Y': '-2'},
    'T': {'A': '0', 'C': '-1', 'D': '-1', 'E': '-1', 'F': '-2', 'G': '-2', 'H': '-2', 'I': '-1', 'K': '-1', 'L': '-1',
          'M': '-1', 'N': '0', 'P': '-1', 'Q': '-1', 'R': '-1', 'S': '1', 'T': '5', 'V': '0', 'W': '-2', 'Y': '-2'},
    'V': {'A': '0', 'C': '-1', 'D': '-3', 'E': '-2', 'F': '-1', 'G': '-3', 'H': '-3', 'I': '3', 'K': '-2', 'L': '1',
          'M': '1', 'N': '-3', 'P': '-2', 'Q': '-2', 'R': '-3', 'S': '-2', 'T': '0', 'V': '4', 'W': '-3', 'Y': '-1'},
    'W': {'A': '-3', 'C': '-2', 'D': '-4', 'E': '-3', 'F': '1', 'G': '-2', 'H': '-2', 'I': '-3', 'K': '-3', 'L': '-2',
          'M': '-1', 'N': '-4', 'P': '-4', 'Q': '-2', 'R': '-3', 'S': '-3', 'T': '-2', 'V': '-3', 'W': '11', 'Y': '2'},
    'Y': {'A': '-2', 'C': '-2', 'D': '-3', 'E': '-2', 'F': '3', 'G': '-3', 'H': '2', 'I': '-1', 'K': '-2', 'L': '-1',
          'M': '-1', 'N': '-2', 'P': '-3', 'Q': '-1', 'R': '-2', 'S': '-2', 'T': '-2', 'V': '-1', 'W': '2', 'Y': '7'}}


def alignment_affine_gap(v, w, sigma=1, scoring_matrix=None, matches=1, mismatches=1, epsilon=1):
    len_v = len(v)
    len_w = len(w)
    lower = np.zeros((len_v + 1, len_w + 1), dtype=float)
    upper = np.zeros((len_v + 1, len_w + 1), dtype=float)
    middle = np.zeros((len_v + 1, len_w + 1), dtype=float)
    backtrack = [[""] * (len_w + 1) for i in range(len_v + 1)]
    # print(backtrack)

    for i in range(1, len(v)+1):
        lower[i][0] = -(sigma + (i-1)*epsilon)
        middle[i][0] = -(sigma + (i-1)*epsilon)
        upper[i][0] = -float("inf")

    for j in range(1, len(w)+1):
        upper[0][j] = -(sigma + (j-1)*epsilon)
        middle[0][j] = -(sigma + (j-1)*epsilon)
        lower[0][j] = -float("inf")

    for i in range(1, len_v + 1):
        for j in range(1, len_w + 1):
            match = (
                int(scoring_matrix[v[i - 1]][w[j - 1]]) if scoring_matrix
                else matches if v[i - 1] == w[j - 1] else mismatches
            )

            lower[i][j] = max(lower[i-1][j] - epsilon,
                              middle[i-1][j] - sigma)
            upper[i][j] = max(upper[i][j-1] - epsilon,
                              middle[i][j-1] - sigma)

            options = [lower[i][j], middle[i-1][j-1] + match, upper[i][j]]
            middle[i][j] = max(options)

            if middle[i][j] == options[0]:
                backtrack[i][j] = "↓"
            elif middle[i][j] == options[1]:
                backtrack[i][j] = "↘"
            elif middle[i][j] == options[2]:
                backtrack[i][j] = "→"

    score_max = int(middle[-1][-1])
    i = len_v
    j = len_w
    # print(s, backtrack)
    while i != 0 and j != 0:
        if backtrack[i][j] == "↓":  # first option lower
            i -= 1
            w = w[:j] + "-" + w[j:]
        elif backtrack[i][j] == "→":  # second option upper
            j -= 1
            v = v[:i] + "-" + v[i:]
        else:  # third option middle
            i -= 1
            j -= 1

    for i in range(i):
        w = w[:0] + "-" + w[0:]

    for i in range(j):
        v = v[:0] + "-" + v[0:]

    return score_max, v, w


with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\alignmentwithaffinegap.txt", "r") as file:
    stringone = file.readline().strip()
    stringtwo = file.readline().strip()
file.close()

with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\alignmentwithaffinegapanswer.txt", "w") as outputfile:
    answer = alignment_affine_gap(stringone, stringtwo, epsilon=1,
                                  sigma=11, scoring_matrix=blosum62_matrix)
    outputfile.write(('\n'.join(map(str, answer))))
outputfile.close()

print('\n'.join(map(str, answer)))
