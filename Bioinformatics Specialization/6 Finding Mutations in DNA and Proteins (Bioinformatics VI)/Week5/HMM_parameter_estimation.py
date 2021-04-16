'''
CODE CHALLENGE: Solve the HMM Parameter Estimation Problem.
Input: A string x of symbols emitted from an HMM, followed by the HMM's alphabet Σ,
     followed by a path π, followed by the collection of states of the HMM.
Output: A transition matrix Transition followed by an emission matrix Emission that maximize
     Pr(x, π) over all possible transition and emission matrices.
'''
import numpy as np
import pandas as pd


def HMM_parameter_estimation(string, alphabet, hidden_path, states):
    if type(alphabet) == str:
        alphabet = alphabet.split(' ')
    if type(states) == str:
        states = states.split(' ')

    transition_matrix = np.full([len(states), len(states)], 0, float)
    transition_matrix = pd.DataFrame(transition_matrix, index=states, columns=states)

    state_emission_matrix = np.full([len(states), len(alphabet)], 0, float)
    state_emission_matrix = pd.DataFrame(state_emission_matrix, index=states, columns=alphabet)

    for i in range(len(hidden_path) - 1):
        current_state = hidden_path[i]
        next_state = hidden_path[i + 1]
        transition_matrix.at[current_state,
                             next_state] = transition_matrix.at[current_state, next_state] + 1

    for state, emission in zip(hidden_path, string):
        state_emission_matrix.at[state, emission] = state_emission_matrix.at[state, emission] + 1

    for i in range(len(states)):
        if sum(transition_matrix.iloc[i]) == 0:
            transition_matrix.iloc[i] = transition_matrix.iloc[i] + 1
        if sum(state_emission_matrix.iloc[i]) == 0:
            state_emission_matrix.iloc[i] = state_emission_matrix.iloc[i] + 1

        transition_matrix.iloc[i] = transition_matrix.iloc[i] / sum(transition_matrix.iloc[i])
        state_emission_matrix.iloc[i] = state_emission_matrix.iloc[i] / \
            sum(state_emission_matrix.iloc[i])

    return(transition_matrix, state_emission_matrix)


# string = 'yyzzzyzzyxyxzxyyzzzzyxyxxyyxyxzzyyyzyyyyyxxzzxxyxyxxxzxxxxxxzyzxxxzzxzyzxxxzxzxxxxzyzyxxyxzxxxxxxyxx'
# alphabet = 'x y z'
# hidden_path = 'BABACBABACAACBBBBCBBBCCACCABAABCAAACCACCBBBCBCBCCABBBCAABBCCABBCCBAABABACCCAACCAAABACCBCAABBCCACCABC'
# states = 'A B C'

# transition_matrix, state_emission_matrix = HMM_parameter_estimation(
#     string, alphabet, hidden_path, states)
# print(transition_matrix.to_string())
# print("--------")
# print(state_emission_matrix.to_string())

if __name__ == "__main__":

    with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\hmmparameterestimation.txt", "r") as file:
        string = file.readline().strip()
        alphabet = file.readline().strip()
        hidden_path = file.readline().strip()
        states = file.readline().strip()

    transition_matrix, state_emission_matrix = HMM_parameter_estimation(
        string, alphabet, hidden_path, states)

    print(transition_matrix.to_string())
    print("--------")
    print(state_emission_matrix.to_string())
