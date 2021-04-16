'''
CODE CHALLENGE: Solve the Sequence Alignment with Profile HMM Problem.
Input: A string x followed by a threshold θ and a pseudocount σ, followed by an
     alphabet Σ, followed by a multiple alignment Alignment whose strings are formed from Σ. 
Output: An optimal hidden path emitting x in HMM(Alignment, θ, σ).
'''
import pandas as pd
import numpy as np
from profile_HMM_with_pseudocounts import profile_HMM_with_pseudocounts


def sequence_alignment_profile_HMM(string, threshold, pseudocount, alphabet, alignment):

    string = list(string)
    transition_matrix, states_emission_matrix = profile_HMM_with_pseudocounts(
        threshold, pseudocount, alphabet, alignment)
    transition_col = list(transition_matrix.columns)

    # give emission a number to avoid replication
    for emission in list(set(string)):
        count = 0
        for i in range(len(string)):
            if string[i] == emission:
                string[i] = string[i] + str(count)
                count = count + 1

    probability_matrix = np.full([len(transition_col), len(string) + 1], 0, float)
    probability_matrix = pd.DataFrame(
        probability_matrix, index=transition_col, columns=['0'] + list(string))

    # fill the first colum
    probability_matrix.at['S', '0'] = 1
    for state in transition_col:
        if state[0] != 'D':
            prob = probability_matrix.at['S', '0'] * transition_matrix.at['S',
                                                                          state] * states_emission_matrix.at[state, string[0][0]]
        else:
            prob = -float('Inf')
            current_D_index = transition_col.index(state)
            for prev_state_index in range(current_D_index):
                prev_state = transition_col[prev_state_index]
                prob_D = probability_matrix.at['S', string[0]] * transition_matrix.at['S', state]

                if prob_D > prob:
                    prob = prob_D

        probability_matrix.at[state, string[0]] = prob

    # dynamic programing
    for string_index in range(1, len(string)):
        emission = string[string_index]
        for state in transition_col:
            max_prob = -float('Inf')
            if state[0] != 'D':
                for prev_state in transition_col:
                    prob = probability_matrix.at[prev_state, string[string_index - 1]] * \
                        transition_matrix.at[prev_state, state] * \
                        states_emission_matrix.at[state, emission[0]]
                    if prob > max_prob:
                        max_prob = prob
            else:
                current_D_index = transition_col.index(state)
                for prev_state_index in range(current_D_index):
                    prev_state = transition_col[prev_state_index]
                    prob = probability_matrix.at[prev_state, emission] * \
                        transition_matrix.at[prev_state, state]

                    if prob > max_prob:
                        max_prob = prob

            probability_matrix.at[state, emission] = max_prob

    # backtrack
    last_emission = string[-1]
    max_prob = -float('Inf')
    for state in transition_col:
        prob = probability_matrix.at[state, last_emission] * transition_matrix.at[state, 'E']
        if prob > max_prob:
            max_prob = prob
            last_state = state

    path = [last_state]
    string = string[:-1]
    string = ['0'] + string
    while last_state != 'S':
        if last_state[0] != 'D':
            for prev_state in transition_col:
                prob = probability_matrix.at[prev_state, string[-1]] * transition_matrix.at[prev_state,
                                                                                            last_state] * states_emission_matrix.at[last_state, last_emission[0]]
                if prob == probability_matrix.at[last_state, last_emission]:
                    path.append(prev_state)
                    last_state = prev_state
                    last_emission = string[-1]
                    string = string[:-1]
                    break
        else:
            current_D_index = transition_col.index(last_state)
            for prev_state_index in range(current_D_index):
                prev_state = transition_col[prev_state_index]
                prob = probability_matrix.at[prev_state, last_emission] * \
                    transition_matrix.at[prev_state, last_state]
                if prob == probability_matrix.at[last_state, last_emission]:
                    path.append(prev_state)
                    last_state = prev_state
                    break

    path = path[::-1]
    path = path[1:]

    return(path)


# string = 'AEFDFDC'
# threshold = 0.4
# pseudocount = 0.01
# alphabet = 'A B C D E F'
# alignment = '''ACDEFACADF
# AFDA---CCF
# A--EFD-FDC
# ACAEF--A-C
# ADDEFAAADF'''

# print(*sequence_alignment_profile_HMM(string, threshold, pseudocount, alphabet, alignment))

if __name__ == "__main__":
    with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\sequencealigmentwithprofileHMM.txt", 'r') as file:
        string = file.readline().strip()

        integers = []
        for val in file.readline().split(' '):
            integers.append(val)
        threshold = float(integers[0])
        pseudocount = float(integers[1])

        alphabet = file.readline().strip()

        listans = []
        for line in file.read().splitlines():
            listans.append(line.strip())
        alignment = '\n'.join(listans)

print(*sequence_alignment_profile_HMM(string, threshold, pseudocount, alphabet, alignment))
