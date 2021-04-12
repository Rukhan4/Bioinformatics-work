'''
CODE CHALLENGE: Implement the Viterbi algorithm solving the Decoding Problem.
Input: A string x, followed by the alphabet from which x was constructed,
     followed by the states States, transition matrix Transition, and emission matrix
     Emission of an HMM (Σ, States, Transition, Emission).
Output: A path that maximizes the (unconditional) probability Pr(x, π) over all possible paths π.

Note: You may assume that transitions from the initial state occur with equal probability.
'''
import pandas as pd
import numpy as np


def viterbi_algorithm(string_x, xs, states, transition_matrix, states_emission_matrix):

    # formating all parameters
    if type(xs) == str:
        xs = xs.split(' ')

    if type(states) == str:
        states = states.split(' ')

    transition_matrix = transition_matrix.split('\n')
    for i in range(len(transition_matrix)):
        transition_matrix[i] = transition_matrix[i].split('\t')
        transition_matrix[i] = list(map(float, transition_matrix[i]))

    transition_matrix = pd.DataFrame(transition_matrix, columns=states, index=states)

    states_emission_matrix = states_emission_matrix.split('\n')
    for i in range(len(states_emission_matrix)):
        states_emission_matrix[i] = states_emission_matrix[i].split('\t')
        states_emission_matrix[i] = list(map(float, states_emission_matrix[i]))

    states_emission_matrix = pd.DataFrame(states_emission_matrix, columns=xs, index=states)

    probability_matrix = np.full([len(states), len(string_x)], 0, float)
    probability_matrix = pd.DataFrame(
        probability_matrix, columns=list(range(len(string_x))), index=states)

    # initailize matrix
    for state in states:
        probability_matrix.at[state, 0] = 0.5 * states_emission_matrix.at[state, string_x[0]]

    # dynanmic programing
    for string_index in range(1, len(string_x)):
        emission = string_x[string_index]

        for state in states:
            max_prob = -float('Inf')

            for state_index in range(len(states)):
                prob = probability_matrix.at[states[state_index], string_index - 1] * \
                    transition_matrix.at[states[state_index], state] * \
                    states_emission_matrix.at[state, emission]
                if prob > max_prob:
                    max_prob = prob

            probability_matrix.at[state, string_index] = max_prob

    # find max probability
    max_prob = -float('Inf')
    for state in states:
        if probability_matrix.at[state, len(string_x) - 1] > max_prob:
            max_prob = probability_matrix.at[state, len(string_x) - 1]
            max_state = state

    # backtrack
    hidden_path = max_state
    for string_index in range(len(string_x) - 1, 0, -1):
        emission = string_x[string_index]

        for state in states:
            if probability_matrix.at[max_state, string_index] == probability_matrix.at[state, string_index - 1] * transition_matrix.at[state, max_state] * states_emission_matrix.at[max_state, emission]:
                max_state = state

                break

        hidden_path = max_state + hidden_path

    return(hidden_path)


if __name__ == "__main__":
    string_x = 'yzxxxzyyyzyzzyzxzyxyxzyyzxxxzxxyzzyxxyzxzyxyxzyxxxyyxxzzyzxyzyzxxxzyzxxzyyzyxxxzxxxzyxzzxzyyxyxzyzzx'
    xs = 'x y z'
    states = 'A B C'

    transition_matrix = '''0.071	0.239	0.69
    0.095	0.310	0.595
    0.555	0.260	0.185'''

    states_emission_matrix = '''0.027	0.422	0.551
    0.111	0.446	0.443
    0.349	0.208	0.443'''

    print(viterbi_algorithm(string_x, xs, states, transition_matrix, states_emission_matrix))
