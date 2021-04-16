'''
CODE CHALLENGE: Implement Viterbi learning for estimating the parameters of an HMM.
Input: A number of iterations j, followed by a string x of symbols emitted by an HMM,
     followed by the HMM's alphabet Σ, followed by the HMM's states, followed by initial transition
     and emission matrices for the HMM.
Output: Emission and transition matrices resulting from applying Viterbi learning for j iterations.
'''
import numpy as np
import pandas as pd
from HMM_parameter_estimation import HMM_parameter_estimation


def matrix_to_hidden_path(string, transition_matrix, state_emission_matrix, states):

    prob_matrix = np.full([len(states), len(string)], 0, float)
    for state_i in range(len(states)):
        state = states[state_i]
        prob_matrix[state_i, 0] = (1 / prob_matrix.shape[0]) * \
            state_emission_matrix.at[state, string[0]]

    # dynamic programing
    for string_index in range(1, len(string)):
        current_emission = string[string_index]

        for state_index in range(len(states)):
            state = states[state_index]
            max_prob = -float('Inf')

            for prev_state_index in range(len(states)):
                prev_state = states[prev_state_index]
                prob = prob_matrix[prev_state_index, string_index - 1] * \
                    transition_matrix.at[prev_state, state] * \
                    state_emission_matrix.at[state, current_emission]
                if prob > max_prob:
                    max_prob = prob
            prob_matrix[state_index, string_index] = max_prob

    # find the last state
    current_prob = max(prob_matrix[:, -1])
    state_index = list(prob_matrix[:, -1]).index(current_prob)
    current_state = states[state_index]
    string_index = len(string) - 1
    hidden_path = current_state

    # backtrack
    while string_index != 0:
        current_emission = string[string_index]
        for prev_state_index in range(len(states)):
            prev_state = states[prev_state_index]
            prob = prob_matrix[prev_state_index, string_index - 1] * transition_matrix.at[prev_state,
                                                                                          current_state] * state_emission_matrix.at[current_state, current_emission]
            if prob == current_prob:
                current_state = prev_state
                hidden_path = current_state + hidden_path
                current_prob = prob_matrix[prev_state_index, string_index - 1]
                string_index = string_index - 1

    return(hidden_path)


def viterbi_learning(iterations, string, alphabet, states, initial_transition_matrix, initial_state_emission_matrix):
    alphabet = alphabet.split(' ')
    states = states.split(' ')

    initial_transition_matrix = initial_transition_matrix.split('\n')
    for i in range(len(initial_transition_matrix)):
        initial_transition_matrix[i] = initial_transition_matrix[i].split('\t')
        initial_transition_matrix[i] = list(map(float, initial_transition_matrix[i]))
    initial_transition_matrix = pd.DataFrame(
        initial_transition_matrix, columns=states, index=states)

    initial_state_emission_matrix = initial_state_emission_matrix.split('\n')
    for i in range(len(initial_state_emission_matrix)):
        initial_state_emission_matrix[i] = initial_state_emission_matrix[i].split('\t')
        initial_state_emission_matrix[i] = list(map(float, initial_state_emission_matrix[i]))
    initial_state_emission_matrix = pd.DataFrame(
        initial_state_emission_matrix, columns=alphabet, index=states)

    transition_matrix, state_emission_matrix = initial_transition_matrix, initial_state_emission_matrix

    for i in range(iterations):
        hidden_path = matrix_to_hidden_path(
            string, transition_matrix, state_emission_matrix, states)
        transition_matrix, state_emission_matrix = HMM_parameter_estimation(
            string, alphabet, hidden_path, states)

    return(transition_matrix, state_emission_matrix)


iterations = 100
string = 'yxzxxxyxzyzxyxzzyzzzxzxzyzxxzzyxzzxyxyyyyxxxzxzzxxzzyxxyzyzxzzxyxyzyzzzxyyyyzxxzzzyxzzyzxxxyyyxxyyxx'
alphabet = 'x y z'
states = 'A B'
initial_transition_matrix = '''0.436	0.564
0.953	0.047'''
initial_state_emission_matrix = '''0.367	0.248	0.385
0.401	0.361	0.238'''

transition_matrix, state_emission_matrix = viterbi_learning(
    iterations, string, alphabet, states, initial_transition_matrix, initial_state_emission_matrix)
print(transition_matrix.to_string())
print("--------")
print(state_emission_matrix.to_string())
