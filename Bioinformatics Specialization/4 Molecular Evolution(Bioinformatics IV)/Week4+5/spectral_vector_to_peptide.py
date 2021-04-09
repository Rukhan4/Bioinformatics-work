'''
CODE CHALLENGE: Solve the Peptide Sequencing Problem.
Given: A space-delimited spectral vector Spectrum'.
Return: An amino acid string with maximum score against Spectrum'. For masses with more than one amino acid, any choice may be used.
'''
import numpy as np

mass_AA_table = open(
    r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\Molecular Evolution(Bioinformatics IV)\integer_mass_table.txt", 'r').read()
mass_AA_table = mass_AA_table.split('\n')

mass_AA = dict()
for line in mass_AA_table:
    line = line.split(' ')
    mass_AA[int(line[1])] = line[0]

#mass_AA_table = mass_AA_table.split('\n')
AA_mass = {}
for line in mass_AA_table:
    AA, mass = line.split(' ')
    AA_mass[AA] = int(mass)


def spectral_vector_to_peptide(spectral_vector, mass_AA, AA_mass):
    if type(spectral_vector) == str:
        spectral_vector = spectral_vector.split(' ')
        spectral_vector = list(map(int, spectral_vector))
    spectral_vector = [0] + spectral_vector

    score_vector = [-float('Inf')] * len(spectral_vector)
    score_vector[0] = 0

    # find max score
    for position in range(len(score_vector)):
        for mass in mass_AA.keys():
            if position >= mass:
                if score_vector[position - mass] + spectral_vector[position] > score_vector[position]:
                    score_vector[position] = score_vector[position - mass] + \
                        spectral_vector[position]

    peptide_string = ''

    position = len(spectral_vector) - 1

    # backtrack
    while position != 0:
        current_score = score_vector[position]
        delta_score = spectral_vector[position]
        last_score = current_score - delta_score
        last_position = np.where(np.array(score_vector) == last_score)[0]
        masss = list(position - last_position)
        mass = 0
        for m in masss:
            if m in mass_AA:
                if m > mass:
                    mass = m
        #AA = mass_AA[mass]
        temp = list(mass_AA.items())
        AA = [idx for idx, key in enumerate(temp) if key[0] == mass]
        AA = ''.join(AA)
        peptide_string = AA + peptide_string
        position = position - mass

    return(peptide_string)


# Test
spectral_vector = "0 0 0 4 -2 -3 -1 -7 6 5 3 2 1 9 3 -8 0 3 1 2 1 8"

spectral_vector_to_peptide(spectral_vector, mass_AA, AA_mass)
