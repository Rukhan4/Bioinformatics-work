'''
CODE CHALLENGE: Solve the Probability of an Outcome Given a Hidden Path Problem.
Input: A string x, followed by the alphabet from which x was constructed, followed by
     a hidden path π, followed by the states States and emission matrix Emission of an HMM
     (Σ, States, Transition, Emission).
Output: The conditional probability Pr(x|π) that x will be emitted given that the HMM
     follows the hidden path π.

Note: You may assume that transitions from the initial state occur with equal probability.
'''

import pandas as pd


def probability_of_an_outcome_given_hidden_path(string_x, xs, hidden_path, states, states_emission_matrix):

    if type(xs) == str:
        xs = xs.split(' ')

    if type(states) == str:
        states = states.split(' ')

    states_emission_matrix = states_emission_matrix.split('\n')

    for i in range(len(states_emission_matrix)):
        states_emission_matrix[i] = states_emission_matrix[i].split('\t')
        states_emission_matrix[i] = list(map(float, states_emission_matrix[i]))

    states_emission_matrix = pd.DataFrame(states_emission_matrix, columns=xs, index=states)

    probability = 1
    for i in range(len(string_x)):
        x = string_x[i]
        state = hidden_path[i]

        probability = probability * states_emission_matrix.at[state, x]

    return(probability)


if __name__ == "__main__":

    string_x = 'xzzxxyzzzyyzzyxyzxxxyzyyxxzzxxzzyzyzyxzxxxyxxyxxxy'
    xs = 'x y z'
    hidden_path = 'ABAAAABAAAAAAAABBBAAAAABBBBABABBBABAAABABAAAAABABB'
    states = 'A B'
    states_emission_matrix = '''0.47	0.14	0.39
    0.467	0.455	0.078'''

    print(probability_of_an_outcome_given_hidden_path(
        string_x, xs, hidden_path, states, states_emission_matrix))
