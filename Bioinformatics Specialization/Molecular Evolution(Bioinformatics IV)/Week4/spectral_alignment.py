'''
CODE CHALLENGE: Solve the Spectral Alignment Problem.
Given: A peptide Peptide, a spectral vector Spectrum', and an integer k.
Return: A peptide Peptide' related to Peptide by up to k modifications with maximal score against Spectrum' out of all possibilities.
'''
import numpy as np

mass_AA_table = open(
    r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\Molecular Evolution(Bioinformatics IV)\integer_mass_table.txt", 'r').read()
mass_AA_table = mass_AA_table.split('\n')


AA_mass = {}
for line in mass_AA_table:
    AA, mass = line.split(' ')
    AA_mass[AA] = int(mass)


def spectral_alignment(peptide_string, spectral_vector, k_modif, AA_mass):
    if type(spectral_vector) == str:
        spectral_vector = spectral_vector.split(' ')
        spectral_vector = list(map(int, spectral_vector))
        spectral_vector = [0] + spectral_vector

    score_matrix = np.full([k_modif + 1, len(peptide_string) + 1,
                           len(spectral_vector)], -float('Inf'), float)
    score_matrix[0, 0, 0] = 0

    AA_mass_list = [0]
    prefix_peptide_mass = [0]
    current_mass = 0
    for AA in peptide_string:
        AA_mass_list.append(AA_mass[AA])
        current_mass = current_mass + AA_mass[AA]
        prefix_peptide_mass.append(current_mass)

    # dynamic programming
    for t in range(k_modif + 1):
        for i in range(1, len(peptide_string) + 1):
            for j in range(len(spectral_vector)):
                max_score = -float('Inf')
                if j >= AA_mass_list[i]:
                    max_score = score_matrix[t, i - 1, j - AA_mass_list[i]]
                for jj in range(j):
                    if max_score < score_matrix[t - 1, i - 1, jj]:
                        max_score = score_matrix[t - 1, i - 1, jj]
                score_matrix[t, i, j] = spectral_vector[j] + max_score

    # backtrack
    i = len(prefix_peptide_mass) - 1
    j = len(spectral_vector) - 1
    t = list(score_matrix[:, -1, -1]).index(max(score_matrix[:, -1, -1]))
    modifications = []

    while t != 0:
        score = score_matrix[t, i, j] - spectral_vector[j]

        if score == score_matrix[t, i - 1, j - AA_mass_list[i]]:
            j = j - AA_mass_list[i]
            i = i - 1

        else:
            for jj in range(j - 1):
                if score == score_matrix[t - 1, i - 1, jj]:
                    modifications.append([i, j - prefix_peptide_mass[i]])
                    i = i - 1
                    j = jj
                    t = t - 1
                    break

    modifications = sorted(modifications)

    # insert modification note
    peptide_string = list(peptide_string)
    shift = 0
    for modification in modifications:
        position = modification[0] - 1
        score = modification[1]

        shift = score - shift

        if shift > 0:
            insertion = '(+' + str(shift) + ')'
        else:
            insertion = '(' + str(shift) + ')'

        peptide_string[position] = peptide_string[position] + insertion

    peptide_string = ''.join(peptide_string)

    return(peptide_string)


if __name__ == "__main__":
    peptide_string = "PCCFMLQ"
    spectral_vector = "11 14 -1 -8 5 8 7 5 11 10 15 -6 1 7 12 -8 2 -1 13 7 -9 8 -8 -10 14 3 9 14 11 -5 7 -4 3 15 6 -7 -2 -1 2 10 5 11 10 14 12 11 -2 14 -4 6 13 1 3 1 8 13 6 3 3 -7 3 11 15 -4 10 12 13 -9 -10 14 10 10 -8 1 -5 -7 4 13 6 8 7 1 4 -8 0 11 -6 -3 -3 -9 7 6 15 -6 1 9 11 -3 -1 -10 3 -4 5 -9 14 -7 11 15 -3 8 14 -2 -6 14 -7 5 14 9 10 -10 -8 2 1 3 5 15 1 -10 14 -9 8 3 13 -3 -6 4 -10 8 -3 -9 13 6 15 8 -4 14 -4 3 1 -1 13 3 4 -6 -2 7 1 1 1 10 -9 -1 3 1 12 -4 -7 15 -10 -4 -10 -4 2 5 13 10 -3 -5 3 -3 7 8 10 -3 8 -10 1 1 11 14 14 13 -9 2 13 3 9 3 -4 5 -4 4 5 -6 7 -1 -7 -6 14 6 -3 15 8 12 13 13 3 15 8 13 -4 1 14 10 2 2 15 12 8 -3 2 14 0 -10 -8 15 15 3 12 8 -8 -8 11 -4 -7 4 12 -2 11 11 14 13 3 -6 8 9 -1 -1 5 -9 11 4 1 9 -1 6 2 -5 8 -9 -2 15 -5 -5 -10 13 11 -6 -9 -10 -2 13 -3 -9 -5 11 8 4 3 -1 8 3 13 -9 12 4 1 -9 10 10 -3 15 -8 10 7 7 7 11 -7 2 -5 5 3 -3 -9 -9 7 15 -1 12 15 -8 15 2 9 13 -9 -9 -4 4 5 9 7 13 15 12 -10 -2 0 14 6 1 -9 0 10 6 -8 -1 -9 12 10 12 3 8 -3 -7 4 -5 -10 10 14 -6 -1 3 -8 3 15 4 -7 1 12 0 -6 -6 -5 11 12 2 4 9 -5 6 -7 13 -5 14 5 -4 3 3 7 13 -6 -10 14 7 -4 9 13 -7 -6 -6 14 6 6 6 -7 4 8 15 -1 -9 3 15 0 13 7 7 8 -8 12 -6 -2 5 8 5 2 6 -9 -3 4 -8 -5 4 12 10 -5 -10 8 11 2 8 3 13 13 2 14 11 0 -6 5 -7 2 14 -8 2 9 9 15 -7 -8 -2 -10 2 -3 12 8 -8 -5 6 8 6 3 1 14 12 12 12 -5 11 -2 5 8 0 -7 -6 14 10 -3 8 6 -7 -5 1 15 4 -6 5 -2 11 1 10 10 -4 -2 -9 15 6 -3 7 13 12 -10 12 -3 -10 3 -9 9 15 -2 15 4 -3 5 3 13 -8 -7 -7 3 6 15 13 11 -9 13 -3 -7 10 -9 12 11 -10 -1 -5 11 -2 10 13 -1 4 10 7 11 -6 6 -8 0 -10 -7 -2 -1 1 -3 11 -6 -2 2 -4 1 -1 5 11 6 -6 -7 12 -8 8 9 -1 11 4 10 1 -3 2 3 1 8 6 -9 11 8 9 5 -1 1 -8 -4 10 -7 14 2 9 10 13 -6 -1 2 7 -1 -4 14 7 3 9 12 -2 -10 6 9 -7 -9 1 10 12 7 1 -10 1 -4 1 0 3 0 6 5 3 5 13 2 -1 1 -1 -9 15 7 11 2 2 -10 1 -2 11 3 3 9 1 12 3 3 -9 8 -5 -1 -2 -6 10 2 10 11 -6 8 -3 -3 -5 7 9 10 0 9 -3 8 8 3 -1 2 1 8 15 -5 5 -3 0 -8 -7 -2 -3 7 -10 -6 8 -3 11 15 6 -9 4 5 -4 -5 1 12 10 -10 2 14 2 -7 -7 11 -3 6 9 -8 0 -9 14 -6 -8 5 5 9 -4 10 -8 15 9 -6 15 -6 2 13 9 1 -7 6 -5 5 12 15 -9 2 -2 -9 12 8 -5 -4 6 13 1 -5 9 9 -2 9 -1 10 -10 15 -7 -5 -1 6 1 -1 7 14 11 -3 6 -2 13 0 9 -3 2 13 12 -7 -6 -1 3 9 14 6 1 8 -4 6 8 0 -3 1 -2 -10 -2 -2 10 6 6 11 7 -10 -6 10 14 13 -6"
    k_modif = 2

    print(spectral_alignment(peptide_string, spectral_vector, k_modif, AA_mass))
