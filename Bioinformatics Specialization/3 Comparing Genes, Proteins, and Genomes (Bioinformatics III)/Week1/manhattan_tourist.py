# Manhattan Tourist Problem -

# Input: Integers n and m, followed by an n × (m + 1) matrix Down and an (n + 1) × m matrix Right.
# The two matrices are separated by the "-" symbol.

# Output: The length of a longest path from source (0, 0) to sink (n, m) in the rectangular grid
# whose edges are defined by the matrices Down and Right.

import numpy as np


def manhattan_tourist(n, m, down, right):
    """
    n × (m + 1) matrix Down
    (n + 1) × m matrix Right
    """

    s = np.zeros((n+1, m+1), dtype=int)
    for i in range(1, n+1):
        s[i][0] = s[i-1][0] + down[i-1][0]
    for j in range(1, m+1):
        s[0][j] = s[0][j-1] + right[0][j-1]

    for i in range(1, n+1):
        for j in range(1, m+1):
            s[i][j] = max(s[i-1][j] + down[i-1][j], s[i][j-1] + right[i][j-1])
            # + Diagonal[i-1][j-1] for longest path

    return s[n, m]


# Answer formatting

filename = open(
    r'C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\manhattantourist.txt', "r")
raw_input = filename.read()
splitting = raw_input.split("-")

# storing the right matrix in prescribed matrix format
right = splitting[1].split("\n")[1:-1]
right_weights = []
for x in right:
    right_weights.append(x.split())

right_weights = np.array(right_weights, dtype=int)

row, col = splitting[0].split("\n")[0].split()
row = int(row)
col = int(col)

# storing the down matrix in prescribed matrix format

down = splitting[0].split("\n")[1:-1]
down_weights = []
for x in down:
    down_weights.append(x.split())

down_weights = np.array(down_weights, dtype=int)


print(manhattan_tourist(row, col, down_weights, right_weights))
