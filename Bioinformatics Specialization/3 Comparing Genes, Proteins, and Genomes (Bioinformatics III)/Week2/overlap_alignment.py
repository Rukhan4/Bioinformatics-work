# Overlap Alignment Problem: Construct a highest-scoring overlap alignment between two strings.
# Input: Two strings v and w, each of length at most 1000.

# Output: The score of an optimal overlap alignment of v and w,
# followed by an alignment of a suffix v' of v and a prefix w' of w achieving this maximum score.
# #Use an alignment score in which matches count +1 and both the mismatch and indel penalties are 2.

def overlap_alignment(v, w):

    # Initialize the arrays.
    S = [[0 for repeat_j in range(len(w)+1)] for repeat_i in range(len(v)+1)]
    backtrack = [[0 for repeat_j in range(len(w)+1)] for repeat_i in range(len(v)+1)]

    # Initialize the max score.
    max_score = -3*(len(v) + len(w))

    # Fill in the Score and Backtrack arrays.
    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            # Match score = 1, Mismatch and Indels = -2.
            scores = [S[i-1][j-1] + [-2, 1][v[i-1] == w[j-1]], S[i-1][j] - 2, S[i][j-1] - 2]
            S[i][j] = max(scores)
            backtrack[i][j] = scores.index(S[i][j])

            # Check if we have a new maximum along the last row or column and update accordingly.
            if i == len(v) or j == len(w):
                if S[i][j] > max_score:
                    max_score = S[i][j]
                    max_indices = (i, j)

    # Initialize i and j as their corresponding index of the maximum score.
    i, j = max_indices

    # Initialize the aligned strings as the input strings, removing the unused tails.
    v_aligned, w_aligned = v[:i], w[:j]

    # Quick lambda function to insert indels.
    def insert_indel(word, i): return word[:i] + '-' + word[i:]

    # Backtrack to the first row or column from the highest score in the last row or column.
    while i*j != 0:
        if backtrack[i][j] == 1:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
        elif backtrack[i][j] == 2:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)
        else:
            i -= 1
            j -= 1

    # Remove the unused head the aligned strings.
    v_aligned, w_aligned = v_aligned[i:], w_aligned[j:]

    return str(max_score), v_aligned, w_aligned


with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\overlapalignment.txt", "r") as file:
    stringone, stringtwo = [line.strip() for line in file.readlines()]

answer = overlap_alignment(stringone, stringtwo)

print('\n'.join(map(str, answer)))
