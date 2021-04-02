"""
CODE CHALLENGE: Solve the Size of Spectral Dictionary Problem.
Given: A spectral vector Spectrum', an integer threshold, and an integer max_score.
Return: The size of the dictionary Dictionarythreshold(Spectrum').
"""

import numpy as np

mass_AA_table = open(
    r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\Molecular Evolution(Bioinformatics IV)\integer_mass_table.txt", 'r').read()
mass_AA_table = mass_AA_table.split('\n')


AA_mass = {}
for line in mass_AA_table:
    AA, mass = line.split(' ')
    AA_mass[AA] = int(mass)


def spectral_dict_size(spectral_vector, min_threshold, max_threshold, AA_mass):
    if type(spectral_vector) == str:
        spectral_vector = spectral_vector.split(' ')
        spectral_vector = list(map(int, spectral_vector))
        spectral_vector = [0] + spectral_vector

    size = np.full([len(spectral_vector), max_threshold + 1], 0, int)
    size[0, 0] = 1

    for i in range(1, len(spectral_vector)):
        for t in range(max_threshold + 1):
            new_size = 0
            for mass in AA_mass.values():
                last_i = i - mass
                last_t = t - spectral_vector[i]
                if (last_i >= 0) & (last_t >= 0):
                    if last_t <= max_threshold:
                        new_size = new_size + size[last_i, last_t]
            size[i, t] = new_size

    dict_size = np.sum(size[-1, min_threshold:])

    return(dict_size)


if __name__ == "__main__":
    spectral_vector = "13 12 14 4 2 -10 -8 -2 14 8 -10 14 3 -5 -8 -9 5 14 -5 -6 -1 8 9 -7 14 14 -10 1 8 -3 0 -6 -10 1 0 -9 -2 9 -3 -8 3 -9 3 12 -5 0 -2 3 -4 7 -5 -7 -3 -7 15 3 -4 11 5 -7 -10 14 0 -8 8 10 -1 -8 -4 0 -7 -7 4 2 10 -7 7 1 1 -7 5 0 -5 11 7 -6 -10 3 -5 1 -10 7 3 4 2 -3 13 15 15 14 -5 -5 6 12 -8 -2 0 2 -10 5 -3 14 6 -9 6 -10 8 0 7 -9 7 11 -10 4 -10 -4 -7 -9 4 -6 4 9 3 -1 -8 10 9 -9 4 -8 3 -3 3 0 7 8 -8 -7 6 12 -4 13 4 11 -4 -3 9 -8 -8 7 3 -9 4 15 9 1 -8 -10 -4 -5 -4 4 -5 7 -1 4 -8 0 15 1 7 14 15 8 1 0 -1 11 -9 12 2 2 6 12 0 0 14 1 -7 12 4 13 -4 4 -1 5 2 9 9 7 -10 -10 5 1 6 11 1 1 14 6 -10 8 -6 -6 1 5 -7 -6 0 11 -10 2 -7 11 -4 14 1 7 13 15 -6 -3 -2 1 1 -5 6 6 -1 2 13 14 10 11 -1 -4 -3 -3 -3 14 8 14 -10 6 9 8 -6 -2 11 -4 -10 2 11 2 3 15 -8 12 5 6 10 10 -3 11 14 9 8 3 3 -2 -8 8 7 -5 -1 2 11 8 -8 0 -10 0 0 3 3 -8 14 -10 4 -10 -2 8 -9 -7 -8 12 11 1 -1 3 13 13 5 -7 -2 2 -1 10 13 6 7 -9 6 4 -7 11 15 4 -9 -10 -7 4 1 -7 -10 3 8 -5 11 -7 -9 -1 11 -2 12 -5 -5 4 -2 10 -7 12 0 2 -9 11 14 14 3 12 10 -1 12 13 9 6 13 0 -4 11 -9 -8 13 -7 5 -9 14 -5 14 6 6 -8 -2 10 8 12 10 4 -10 10 -9 11 13 -9 7 -3 13 0 8 -3 6 -3 2 7 11 -5 15 2 -10 -5 7 4 -1 4 0 1 -1 14 6 -7 8 -1 1 9 -1 11 -6 -9 -7 -7 4 8 7 10 1 2 12 5 -1 -8 -9 -3 5 6 -7 9 14 12 10 -1 14 13 8 14 4 4 15 7 -8 -5 8 1 7 12 9 -1 -2 14 13 8 -2 15 11 10 -6 4 14 7 8 -1 2 -7 -9 11 12"
    min_threshold = 37
    max_threshold = 200

    print(spectral_dict_size(spectral_vector, min_threshold, max_threshold, AA_mass))
