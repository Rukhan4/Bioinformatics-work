'''
CODE CHALLENGE: Solve the Outcome Likelihood Problem.
Input: A string x, followed by the alphabet from which x was constructed,
     followed by the states States, transition matrix Transition, and emission matrix
     Emission of an HMM (Σ, States, Transition, Emission).
Output: The probability Pr(x) that the HMM emits x.

Note: You may assume that transitions from the initial state occur with equal probability.
'''
import pandas as pd
import numpy as np


def outcome_likelihood(string_x, xs, states, transition_matrix, states_emission_matrix):
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

    # fill the matrix
    for string_index in range(1, len(string_x)):
        emission = string_x[string_index]

        for state in states:
            sum_prob = 0

            for state_index in range(len(states)):
                prob = probability_matrix.at[states[state_index], string_index - 1] * \
                    transition_matrix.at[states[state_index], state] * \
                    states_emission_matrix.at[state, emission]
                sum_prob = sum_prob + prob

            probability_matrix.at[state, string_index] = sum_prob

    probability = sum(probability_matrix[len(string_x) - 1])

    return(probability)


if __name__ == "__main__":

    string_x = 'xxyyzxyxxxxzyyxxxxyzyxyzxxzxyxyyxyzzyzzyxyzxzyxyxzzyyxzyyxxzxyyyyyxxzyzxyyyzxyyxxzyyzzyyzyxzzxxxzxzy'
    xs = 'x y z'
    states = 'A B C'

    transition_matrix = '''0.427	0.258	0.315
    0.345	0.161	0.494
    0.390	0.411	0.199'''

    states_emission_matrix = '''0.255	0.588	0.157
    0.238	0.539	0.223
    0.079	0.611	0.310'''

print(outcome_likelihood(string_x, xs, states, transition_matrix, states_emission_matrix))
