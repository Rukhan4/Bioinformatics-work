# Edit Distance Problem: Find the edit distance between two strings. ie; how many edits does it take to transform string 1 to string 2

# Input: Two strings.
# Output: The edit distance between these strings.
from numpy import zeros


def edit_distance(v, w):

    # Initialize matrix M.
    M = zeros((len(v)+1, len(w)+1), dtype=int)
    # print(M)

    for i in range(1, len(v)+1):
        M[i][0] = i
    for j in range(1, len(w)+1):
        M[0][j] = j

    # Compute each entry of M.
    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            if v[i-1] == w[j-1]:
                M[i][j] = M[i-1][j-1]
            else:
                M[i][j] = min(M[i-1][j]+1, M[i][j-1]+1, M[i-1][j-1]+1)

    return M[len(v)][len(w)]


#print(edit_distance("PLEASANTLY", "MEANLY"))

with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\editdistance.txt", "r") as file:
    stringone, stringtwo = [line.strip() for line in file.readlines()]

print(edit_distance(stringone, stringtwo))
