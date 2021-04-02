'''
CODE CHALLENGE: Solve the Probability of Spectral Dictionary Problem.
Given: A spectral vector Spectrum', an integer threshold, and an integer max_score.
Return: The probability of the dictionary Dictionarythreshold(Spectrum').
'''
import numpy as np

mass_AA_table = open(
    r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\Molecular Evolution(Bioinformatics IV)\integer_mass_table.txt", 'r').read()
mass_AA_table = mass_AA_table.split('\n')


AA_mass = {}
for line in mass_AA_table:
    AA, mass = line.split(' ')
    AA_mass[AA] = int(mass)


def probability_spectral_dict(spectral_vector, min_threshold, max_threshold, AA_mass):
    if type(spectral_vector) == str:
        spectral_vector = spectral_vector.split(' ')
        spectral_vector = list(map(int, spectral_vector))
        spectral_vector = [0] + spectral_vector

    prob = np.full([len(spectral_vector), max_threshold + 1], 0, float)
    prob[0, 0] = 1

    for i in range(1, len(spectral_vector)):
        for t in range(max_threshold + 1):
            new_prob = 0
            for mass in AA_mass.values():
                last_i = i - mass
                last_t = t - spectral_vector[i]

                if (last_i >= 0) & (last_t >= 0):
                    if last_t <= max_threshold:
                        new_prob = new_prob + prob[last_i, last_t]

            prob[i, t] = (new_prob) / len(AA_mass.values())

    dict_prob = np.sum(prob[-1, min_threshold:])

    return(dict_prob)


if __name__ == "__main__":
    spectral_vector = "-6 5 11 -10 -8 15 6 -8 -6 13 -5 -8 -8 -10 -4 11 0 -7 -10 -1 15 1 -2 -9 -6 10 -4 -9 -7 6 3 9 8 -3 3 12 10 7 -1 11 -2 13 2 -1 -4 14 7 -8 5 -2 -1 10 -4 -5 6 2 -2 -5 7 -2 6 -10 -2 3 -2 -5 -6 -3 0 -10 8 11 -5 -3 -2 4 -7 7 -8 -1 -1 12 13 0 2 14 5 -1 0 -1 14 15 -4 -4 10 2 -8 8 4 -4 -3 -1 -5 13 -6 11 -4 15 -6 3 13 3 1 -6 11 6 -6 -2 12 -10 14 7 -2 -5 15 11 -1 -3 10 -10 -7 11 15 2 10 7 6 5 0 15 6 7 10 10 15 7 0 2 13 14 4 -1 2 4 -1 6 -9 0 6 -4 11 5 -1 -1 8 9 1 -10 3 -1 -10 -5 1 -6 14 -3 -1 10 1 -2 -8 -4 -9 -2 -3 13 11 13 10 -6 -8 9 5 9 5 1 5 8 15 -10 5 3 10 -8 -7 3 3 9 8 -4 -6 -6 -5 4 -2 -3 12 0 6 12 -10 -7 0 11 -4 -2 12 0 -6 1 8 9 14 -9 -6 -2 9 -1 -8 -9 2 1 -3 1 8 0 -1 -9 0 -8 6 -6 -1 -4 -1 8 -6 3 4 8 13 14 13 7 6 -6 6 -3 13 2 -6 -6 5 1 5 1 11 2 8 15 15 8 -10 5 14 15 9 0 -5 3 8 4 -9 8 2 11 10 0 -1 -2 6 12 -3 -6 4 -1 15 1 12 10 -2 8 -3 -1 -1 -2 7 -8 3 5 9 -9 15 12 5 5 -2 2 -6 -4 -10 8 -4 14 -7 8 -7 -1 10 12 -7 7 7 -1 5 15 -8 3 -1 -7 -4 -1 5 5 4 4 -1 -3 6 -6 -4 -6 15 13 -7 -2 5 0 6 9 5 -10 -10 8 -8 12 -9 7 11 14 -1 0 4 -10 -3 -4 -8 0 13 0 8 3 1 -6 10 3 -1 -2 -2 -1 12 -5 1 4 2 12 2 5 15 10 -7 10 -3 13 -4 2 1 12 -5 9 -2 12 5 2 -2 7 -3 13 -1 6 -9 -8 7 -1 -1 9 15 -1 10 1 11 0 10 11 2 -6 -3 4 14 5 -9 -7 11 8 3 0 7 10 1 15 3 10 -6 0 5 -1 15 -5 12 15 15 -5 -8 -7 -1 -3 11 10 3 -9 13 15 12 -10 12 10 6 -4 6 -9 -2 4 -10 6 5 12 12 -9 15 -4"
    min_threshold = 40
    max_threshold = 200

    print(probability_spectral_dict(spectral_vector, min_threshold, max_threshold, AA_mass))
