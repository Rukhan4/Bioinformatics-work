def MultipleLongestCommonSubsequence_simplest(seq1, seq2, seq3):
    len1 = len(seq1)
    len2 = len(seq2)
    len3 = len(seq3)

    # part 1: create backtrack matrix

    # backtrack matrix with blank initial values
    bt = [[['_'] * len3 for j in range(len2)]
          for i in range(len1)
          ]

    # score matrix with blank initial values
    s = [[[0] * (len3 + 1) for j in range(len2 + 1)]
         for i in range(len1 + 1)
         ]

    # fill in matrices cell by cell
    for i, ch1 in enumerate(seq1, start=1):
        for j, ch2 in enumerate(seq2, start=1):
            for k, ch3 in enumerate(seq3, start=1):
                match = 1 if (ch1 == ch2 == ch3) else 0
                cs = max(s[i][j-1][k-1],           # cs -current value in score matrix
                         s[i-1][j][k-1],  # =s[i][j][k]
                         s[i-1][j-1][k],
                         s[i][j][k-1],
                         s[i][j-1][k],
                         s[i-1][j][k],
                         s[i-1][j-1][k-1] + match)

                if cs == s[i-1][j-1][k-1] + match:
                    cbt = 'd'                      # cbt -current value in backtrack matrix
                elif cs == s[i][j-1][k-1]:  # =bt[i-1][j-1][k-1]
                    cbt = '⇒'
                elif cs == s[i-1][j][k-1]:
                    cbt = '⇓'
                elif cs == s[i-1][j-1][k]:
                    cbt = '↘'
                elif cs == s[i][j][k-1]:
                    cbt = '⨂'
                elif cs == s[i][j-1][k]:
                    cbt = '→'
                elif cs == s[i-1][j][k]:
                    cbt = '↓'
                else:
                    raise ValueError('something wrong in calculation')

                s[i][j][k] = cs
                bt[i-1][j-1][k-1] = cbt

    # part 2: distribute gaps in the sequences and calculate score

    i, j, k = len1 - 1, len2 - 1, len3 - 1
    seq1_mod = seq2_mod = seq3_mod = ''   # modified versions of strings
    sc = 0                                # score

    while i != -1 and j != -1 and k != -1:
        ch = bt[i][j][k]
        if ch == '↓':
            seq1_mod += seq1[i]
            seq2_mod += '-'
            seq3_mod += '-'
            i -= 1
        elif ch == '→':
            seq1_mod += '-'
            seq2_mod += seq2[j]
            seq3_mod += '-'
            j -= 1
        elif ch == '⨂':
            seq1_mod += '-'
            seq2_mod += '-'
            seq3_mod += seq3[k]
            k -= 1
        elif ch == '↘':
            seq1_mod += seq1[i]
            seq2_mod += seq2[j]
            seq3_mod += '-'
            i -= 1
            j -= 1
        elif ch == '⇓':
            seq1_mod += seq1[i]
            seq2_mod += '-'
            seq3_mod += seq3[k]
            i -= 1
            k -= 1
        elif ch == '⇒':
            seq1_mod += '-'
            seq2_mod += seq2[j]
            seq3_mod += seq3[k]
            j -= 1
            k -= 1
        elif ch == 'd':
            seq1_mod += seq1[i]
            seq2_mod += seq2[j]
            seq3_mod += seq3[k]
            if seq1[i] == seq2[j] == seq3[k]:
                sc += 1
            i -= 1
            j -= 1
            k -= 1
        else:
            raise ValueError(f'Unrecognize symbol in matrix: {ch}')

    # finalize lines after previous loop (simplest approach)
    while i >= 0 or j >= 0 or k >= 0:
        if (j == -1) and (k == -1):
            seq1_mod += seq1[i]
            seq2_mod += '-'
            seq3_mod += '-'
            i -= 1
        elif (i == -1) and (k == -1):
            seq1_mod += '-'
            seq2_mod += seq2[j]
            seq3_mod += '-'
            j -= 1
        elif (i == -1) and (j == -1):
            seq1_mod += '-'
            seq2_mod += '-'
            seq3_mod += seq3[k]
            k -= 1
        elif k == -1:
            seq1_mod += seq1[i]
            seq2_mod += seq2[j]
            seq3_mod += '-'
            i -= 1
            j -= 1
        elif j == -1:
            seq1_mod += seq1[i]
            seq2_mod += '-'
            seq3_mod += seq3[k]
            i -= 1
            k -= 1
        elif i == -1:
            seq1_mod += '-'
            seq2_mod += seq2[j]
            seq3_mod += seq3[k]
            j -= 1
            k -= 1
        else:
            raise ValueError(f'Something wrong at the step of finalization of lines')

    return seq1_mod[::-1], seq2_mod[::-1], seq3_mod[::-1], sc


with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\mlcsp.txt", "r") as file:
    seq1 = file.readline().strip()
    seq2 = file.readline().strip()
    seq3 = file.readline().strip()


seq1_mod, seq2_mod, seq3_mod, sc = MultipleLongestCommonSubsequence_simplest(seq1, seq2, seq3)
print(sc)
print(seq1_mod)
print(seq2_mod)
print(seq3_mod)
