seq1 = "AACCTTGG"
seq2 = "ACACTGTGA"


def LCSBackTrack(seq1, seq2):
    backtrack = [['.']*len(seq2) for _ in range(len(seq1))]
    s = [[0]*(len(seq2)+1) for _ in range(len(seq1)+1)]  # score
    # the last row and column of 's' contain zeros that are necessary
    # for correct work of the below loop

    for i, ch1 in enumerate(seq1):
        for j, ch2 in enumerate(seq2):
            match = 1 if (ch1 == ch2) else 0
            s[i][j] = max(s[i-1][j], s[i][j-1], s[i-1][j-1] + match)
            if s[i][j] == s[i-1][j]:
                backtrack[i][j] = '↓'
            elif s[i][j] == s[i][j-1]:
                backtrack[i][j] = '→'
            else:                        # s[i][j] == s[i-1][j-1] + match
                backtrack[i][j] = '↘'

    return backtrack


backtrack = LCSBackTrack(seq1, seq2)


def OutputLCS(backtrack, seq1, seq2):
    # seq2 is used only for checking of correctness of data

    i = len(backtrack) - 1
    j = len(backtrack[0]) - 1
    lcs = ''

    while i != -1 and j != -1:
        ch = backtrack[i][j]
        if ch == '↓':
            i -= 1
        elif ch == '→':
            j -= 1
        elif ch == '↘':
            assert seq1[i] == seq2[j], 'Characters in seq1[i] and seq2[j] are not matched'
            lcs += seq1[i]
            i -= 1
            j -= 1
        else:
            pass

    return lcs[::-1]


print(OutputLCS(backtrack, seq1, seq2))
