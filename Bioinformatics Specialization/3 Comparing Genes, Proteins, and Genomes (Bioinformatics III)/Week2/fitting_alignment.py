# Solve the Fitting Alignment Problem.

# Input: Two nucleotide strings v and w, where v has length at most 1000 and w has length at most 100.
# Output: A highest-scoring fitting alignment between v and w.

# Use the simple scoring method in which matches count +1 and
# both the mismatch and indel penalties are 1

from numpy import zeros


def fitting_alignment(v, w):

    # Initialize the matrices.
    S = zeros((len(v)+1, len(w)+1), dtype=int)
    backtrack = zeros((len(v)+1, len(w)+1), dtype=int)

    # Fill in the Score and Backtrack matrices.
    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            scores = [S[i-1][j] - 1, S[i][j-1] - 1, S[i-1][j-1] + [-1, 1][v[i-1] == w[j-1]]]
            S[i][j] = max(scores)
            backtrack[i][j] = scores.index(S[i][j])

    # Get the position of the highest scoring cell corresponding to the end of the shorter word w.
    j = len(w)
    i = max(enumerate([S[row][j] for row in range(len(w), len(v))]),
            key=lambda x: x[1])[0] + len(w)
    max_score = str(S[i][j])

    # Initialize the aligned strings as the input strings up to the position of the high score.
    v_aligned, w_aligned = v[:i], w[:j]

    # insert indels.
    def insert_indel(word, i):
        return word[:i] + '-' + word[i:]

    # Backtrack to start of the fitting alignment.
    while i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
        elif backtrack[i][j] == 1:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)
        elif backtrack[i][j] == 2:
            i -= 1
            j -= 1

    # Cut off v at the ending point of the backtrack.
    v_aligned = v_aligned[i:]

    return max_score, v_aligned, w_aligned


with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\fittingalignment.txt", "r") as file:
    stringone, stringtwo = [line.strip() for line in file.readlines()]
answer = fitting_alignment(stringone, stringtwo)

print('\n'.join(map(str, answer)))
