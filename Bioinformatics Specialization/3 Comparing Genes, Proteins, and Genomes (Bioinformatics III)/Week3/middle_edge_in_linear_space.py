# Middle Edge In Linear Space Problem -

# Input: Two amino acid strings.

# Output: A middle edge in the alignment graph in the form "(i, j) (k, l)",
# where (i, j) connects to (k, l). To compute scores,
# use the BLOSUM62 scoring matrix and a (linear) indel penalty equal to 5.


def Blosum62():
    B62 = {}
    with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\Comparing Genes, Proteins and Genomes (Bioinformatics III)\BLOSUM62.txt", 'r') as file:
        AA = file.readline().strip().split('  ')
        arrays = []
        for _ in AA:
            array = list(file.readline().strip().split(' '))
            while '' in array:
                array.remove('')
            array = list(int(i) for i in array[1:])
            arrays.append(array)
    for i in range(len(AA)):
        for j in range(len(AA)):
            B62[(AA[i], AA[j])] = arrays[i][j]
    return B62


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


def Mid_Edge(v, w):

    def Paths_to_mid(v, w):

        S = [[0, -sigma]] + list([-sigma*i, -float('inf')] for i in range(1, len(v)+1))
        for j in range(1, len(w)+1):
            for i in range(len(v)+1):

                match = scoring_matrix[(v[i-1], w[j-1])]

                S[i][j % 2] = max(
                    S[i-1][j % 2] - sigma,
                    S[i][(j-1) % 2] - sigma,
                    S[i-1][(j-1) % 2] + match)

        return list(S[i][j % 2] for i in range(len(v)+1))

    mid_j = len(w)//2

    From_Source = Paths_to_mid(v, w[:mid_j])
    To_Sink = Paths_to_mid(v[::-1], w[len(w):mid_j-1:-1])
    To_Sink.reverse()

    best = -float('inf')
    for i in range(len(v)+1):
        len_ipath = From_Source[i] + To_Sink[i]
        if len_ipath >= best:
            best = len_ipath
            mid_i = i

    score = max(-sigma, scoring_matrix[(v[mid_i], w[mid_j])])

    if score == -sigma:
        return (mid_i, mid_j), (mid_i, mid_j+1)
    else:
        return (mid_i, mid_j), (mid_i+1, mid_j+1)


with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\middle_edge_dataset.txt", 'r') as infile:
    v = infile.readline().strip()
    w = infile.readline().strip()

sigma = 5
scoring_matrix = blosum62_matrix
Edge = Mid_Edge(v, w)
print(' '.join(str(e) for e in Edge))
