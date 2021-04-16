'''
CODE CHALLENGE: Solve the Soft Decoding Problem.
Input: A string x, followed by the alphabet Σ from which x was constructed,
     followed by the states States, transition matrix Transition, and emission matrix
     Emission of an HMM (Σ, States, Transition, Emission).
Output: An |x| x |States| matrix whose (i, k)-th element holds the conditional probability Pr(πi = k|x).
'''
import numpy as np
import pandas as pd


def forward_probability(string, alphabet, states, transition_matrix, state_emission_matrix):
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
            sum_prob = 0
            for prev_state_index in range(len(states)):
                prev_state = states[prev_state_index]
                prob = prob_matrix[prev_state_index, string_index - 1] * \
                    transition_matrix.at[prev_state, state] * \
                    state_emission_matrix.at[state, current_emission]
                sum_prob = sum_prob + prob
            prob_matrix[state_index, string_index] = sum_prob

    return(prob_matrix)


def backward_probability(string, alphabet, states, transition_matrix, state_emission_matrix):
    prob_matrix = np.full([len(states), len(string)], 0, float)
    backward_string = string[::-1]

    for state_i in range(len(states)):
        prob_matrix[state_i, 0] = 1

    # dynamic programing
    for string_index in range(1, len(backward_string)):
        current_emission = backward_string[string_index - 1]

        for state_index in range(len(states)):
            state = states[state_index]
            sum_prob = 0
            for prev_state_index in range(len(states)):
                prev_state = states[prev_state_index]
                prob = prob_matrix[prev_state_index, string_index - 1] * transition_matrix.at[state,
                                                                                              prev_state] * state_emission_matrix.at[prev_state, current_emission]
                sum_prob = sum_prob + prob
            prob_matrix[state_index, string_index] = sum_prob

    prob_matrix = np.flip(prob_matrix, 1)

    return(prob_matrix)


def soft_decoding_HMM(string, alphabet, states, transition_matrix, state_emission_matrix):
    alphabet = alphabet.split(' ')
    states = states.split(' ')

    transition_matrix = transition_matrix.split('\n')
    for i in range(len(transition_matrix)):
        transition_matrix[i] = transition_matrix[i].split('\t')
        transition_matrix[i] = list(map(float, transition_matrix[i]))
    transition_matrix = pd.DataFrame(transition_matrix, columns=states, index=states)

    state_emission_matrix = state_emission_matrix.split('\n')
    for i in range(len(state_emission_matrix)):
        state_emission_matrix[i] = state_emission_matrix[i].split('\t')
        state_emission_matrix[i] = list(map(float, state_emission_matrix[i]))
    state_emission_matrix = pd.DataFrame(state_emission_matrix, columns=alphabet, index=states)

    #
    forward_prob_matrix = forward_probability(
        string, alphabet, states, transition_matrix, state_emission_matrix)
    backward_prob_matrix = backward_probability(
        string, alphabet, states, transition_matrix, state_emission_matrix)

    prob_forwad_sink = sum(forward_prob_matrix[:, -1])

    prob_matrix = np.full([len(states), len(string)], 0, float)
    for i in range(len(string)):

        for k_index in range(len(states)):
            forward_probability_k_i = forward_prob_matrix[k_index, i]
            backward_probability_k_i = backward_prob_matrix[k_index, i]

            prob_matrix[k_index, i] = forward_probability_k_i * \
                backward_probability_k_i / prob_forwad_sink

        #prob_matrix[:, i] = prob_matrix[:, i] / sum(prob_matrix[:, i])

    return(prob_matrix)


if __name__ == "__main__":

    string = 'zyxyyzxxxy'
    alphabet = 'x y z'
    states = 'A B C D'
    transition_matrix = '''0.449	0.009	0.029	0.513
    0.080	0.396	0.391	0.133
    0.233	0.189	0.272	0.306
    0.274	0.146	0.263	0.317'''
    state_emission_matrix = '''0.217	0.484	0.299
    0.392	0.081	0.527
    0.164	0.520	0.316
    0.369	0.342	0.289'''

    result = soft_decoding_HMM(string, alphabet, states, transition_matrix, state_emission_matrix)
    for i in result.T:  # transpose for formatting
        print(*i)
