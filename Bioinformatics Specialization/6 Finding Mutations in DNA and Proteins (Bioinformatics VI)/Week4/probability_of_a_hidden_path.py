'''
CODE CHALLENGE: Solve the Probability of a Hidden Path Problem.
Given: A hidden path π followed by the states States and transition matrix Transition of an HMM
     (Σ, States, Transition, Emission).
Return: The probability of this path, Pr(π).

Note: You may assume that transitions from the initial state occur with equal probability.
'''

import pandas as pd


def probability_of_a_hidden_path(hidden_path, states, transition_matrix):

    if type(states) == str:
        states = states.split(' ')

    transition_matrix = transition_matrix.split('\n')

    for i in range(len(transition_matrix)):
        transition_matrix[i] = transition_matrix[i].split('\t')
        transition_matrix[i] = list(map(float, transition_matrix[i]))

    transition_matrix = pd.DataFrame(transition_matrix, columns=states, index=states)

    probability = 0.5
    for i in range(len(hidden_path) - 1):
        current_state = hidden_path[i]
        next_state = hidden_path[i + 1]
        probability = probability * transition_matrix.at[current_state, next_state]

    return(probability)


if __name__ == "__main__":
    hidden_path = 'ABBAAAABBABBABAABAAABBABBABAABBABBBBAABABAAAABABAA'
    states = 'A B'
    transition_matrix = '''0.544	0.456
    0.581	0.419'''

    print(probability_of_a_hidden_path(hidden_path, states, transition_matrix))
