'''
CODE CHALLENGE: Solve the Profile HMM Problem.
Input: A threshold θ, followed by an alphabet Σ, followed by a multiple alignment
     Alignment whose strings are formed from Σ.
Output: The transition matrix followed by the emission matrix of HMM(Alignment, θ).
'''
import pandas as pd
import numpy as np


def profile_HMM(threshold, alphabet, alignment):

    # formatting inputs
    if type(alphabet) == str:
        alphabet = alphabet.split(' ')

    if type(alignment) == str:
        alignment = alignment.split('\n')

    for i in range(len(alignment)):
        alignment[i] = list(alignment[i])
    alignment = np.array(alignment)

    # find insertion columns by threshold
    insertion_col = []
    for j in range(alignment.shape[1]):
        count = 0
        for i in range(alignment.shape[0]):
            if alignment[i, j] == '-':
                count = count + 1
        if (count / alignment.shape[0]) >= threshold:
            insertion_col.append(j)

    n_M = len(alignment[0]) - len(insertion_col)

    # build transition_matrix and emission_matrix
    transition_col = ['S', 'I0']
    for n in range(1, n_M + 1):
        for node in ['M', 'D', 'I']:
            transition_col.append(node + str(n))
    transition_col.append('E')

    transition_matrix = np.full([len(transition_col), len(transition_col)], 0, float)
    transition_matrix = pd.DataFrame(
        transition_matrix, columns=transition_col, index=transition_col)

    emission_matrix = np.full([len(transition_col), len(alphabet)], 0, float)
    emission_matrix = pd.DataFrame(emission_matrix, columns=alphabet, index=transition_col)

    # fill transition_matrix and emission_matrix by count
    for string in alignment:

        states = []
        M_count = 0

        for i in range(len(string)):
            base = string[i]
            if i in insertion_col:
                if base != '-':
                    state = 'I' + str(M_count)
                    states.append(state)
                    emission_matrix.at[state, string[i]] = emission_matrix.at[state, string[i]] + 1

            elif base != '-':
                M_count = M_count + 1
                state = 'M' + str(M_count)
                states.append(state)
                emission_matrix.at[state, string[i]] = emission_matrix.at[state, string[i]] + 1

            else:
                M_count = M_count + 1
                state = 'D' + str(M_count)
                states.append(state)

        current_state = 'S'

        for state in states:
            transition_matrix.at[current_state,
                                 state] = transition_matrix.at[current_state, state] + 1
            current_state = state

        transition_matrix.at[current_state, 'E'] = transition_matrix.at[current_state, 'E'] + 1

    # normalize transition_matrix and emission_matrix
    for i in range(len(transition_col)):
        if sum(transition_matrix.iloc[i]) != 0:
            transition_matrix.iloc[i] = transition_matrix.iloc[i] / sum(transition_matrix.iloc[i])

        if sum(emission_matrix.iloc[i]) != 0:
            emission_matrix.iloc[i] = emission_matrix.iloc[i] / sum(emission_matrix.iloc[i])

    return(transition_matrix, emission_matrix)

#threshold = 0.291
#alphabet = 'A B C D E'
# alignment = '''D-E-DCCE-
# EA-CDCDAE
# DCBBDC-E-
# DBECECCEE
# DBECDCCCE
# E--AD-C-E
# DADCECCEE
# -EEDD--DE
# EBA-D-CCB
# DBECDCC--'''


if __name__ == "__main__":

    #transition_matrix, emission_matrix = profile_HMM(threshold, alphabet, alignment)
    with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\profileHMM.txt", "r") as in_file:
        threshold = float(in_file.readline().strip())

        alphabet = in_file.readline().strip()

        listans = []
        for line in in_file.read().splitlines():
            listans.append(line.strip())
        alignment = '\n'.join(listans)

    transition_matrix, emission_matrix = profile_HMM(threshold, alphabet, alignment)

    # with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\profileHMManswer.txt", "w") as file:
    #     file.write(transition_matrix.to_string())
    #     file.write(emission_matrix.to_string())
    # file.close()

    print(transition_matrix.to_string())
    print("-------")
    print(emission_matrix.to_string())
