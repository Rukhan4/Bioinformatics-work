""" 
We will also add pseudocounts to the matrix of emission probabilities and normalize the resulting matrix. We refer to the profile HMM defined by the resulting normalized matrices of transition and emission probabilities as HMM(Alignment, θ, σ).

Profile HMM with Pseudocounts Problem: Construct a profile HMM with pseudocounts from a multiple alignment.

Input: A multiple alignment Alignment, a threshold value θ, and a pseudocount value σ.
Output: HMM(Alignment, θ), in the form of transition and emission matrices.
Code Challenge: Solve the Profile HMM with Pseudocounts Problem.

Input: A threshold θ and a pseudocount σ, followed by an alphabet Σ, followed by a multiple alignment Alignment whose strings are formed from Σ.
Output: The transition and emission matrices of HMM(Alignment, θ, σ).
"""
import pandas as pd
from profile_HMM import profile_HMM


def profile_HMM_with_pseudocounts(threshold, pseudocount, alphabet, alignment):

    transition_matrix, emission_matrix = profile_HMM(threshold, alphabet, alignment)
    transition_col = list(transition_matrix.columns)
    n_M = 0
    for state in transition_col:
        if state[0] == 'M':
            n_M = n_M + 1

    # pseudocount
    transition_matrix.iloc[0, 1:4] = transition_matrix.iloc[0, 1:4] / \
        sum(transition_matrix.iloc[0, 1:3]) + pseudocount
    transition_matrix.iloc[0, 1:4] = transition_matrix.iloc[0, 1:4] / \
        sum(transition_matrix.iloc[0, 1:4])

    for i in range(1, len(transition_col[:-1])):
        state = transition_col[i]
        if sum(transition_matrix.iloc[i]) != 0:
            transition_matrix.iloc[i] = transition_matrix.iloc[i] / sum(transition_matrix.iloc[i])

        state_I = 'I' + str(state[1:])
        state_M = 'M' + str(int(state[1:]) + 1)
        state_D = 'D' + str(int(state[1:]) + 1)

        if int(state[1:]) < n_M:
            transition_matrix.at[state,
                                 state_I] = transition_matrix.at[state, state_I] + pseudocount
            transition_matrix.at[state,
                                 state_M] = transition_matrix.at[state, state_M] + pseudocount
            transition_matrix.at[state,
                                 state_D] = transition_matrix.at[state, state_D] + pseudocount
        else:
            transition_matrix.at[state,
                                 state_I] = transition_matrix.at[state, state_I] + pseudocount
            transition_matrix.at[state, 'E'] = transition_matrix.at[state, 'E'] + pseudocount

        transition_matrix.iloc[i] = transition_matrix.iloc[i] / sum(transition_matrix.iloc[i])

        if state[0] != 'D':
            if sum(emission_matrix.iloc[i]) != 0:
                emission_matrix.iloc[i] = (emission_matrix.iloc[i] /
                                           sum(emission_matrix.iloc[i])) + pseudocount
            else:
                emission_matrix.iloc[i] = emission_matrix.iloc[i] + pseudocount

            emission_matrix.iloc[i] = emission_matrix.iloc[i] / sum(emission_matrix.iloc[i])

    return(transition_matrix, emission_matrix)


# threshold = 0.389
# pseudocount = 0.01
# alphabet = 'A B C D E'
# alignment = '''CAD
# AAD
# AAD
# AAD
# ABD
# AAD
# ABD
# -AD
# AAD
# AAD'''

if __name__ == "__main__":
    with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\profileHMMwithpseudocounts.txt", "r") as file:
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

    transition_matrix, emission_matrix = profile_HMM_with_pseudocounts(
        threshold, pseudocount, alphabet, alignment)
    print(transition_matrix.to_string())
    print("--------")
    print(emission_matrix.to_string())
