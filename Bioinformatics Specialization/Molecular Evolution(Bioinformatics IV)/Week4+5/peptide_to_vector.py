"""
CODE CHALLENGE: Solve the Converting a Peptide into a Peptide Vector Problem.
Given: An amino acid string P.
Return: The peptide vector of P (in the form of space-separated integers).
"""
from decoding_ideal_spectrum import linear_spectrum

mass_AA_table = open(
    r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\Molecular Evolution(Bioinformatics IV)\integer_mass_table.txt", 'r').read()
mass_AA_table = mass_AA_table.split('\n')

AA_mass = {}
for line in mass_AA_table:
    AA, mass = line.split(' ')
    AA_mass[AA] = int(mass)


def peptide_to_vector(peptide_string, AA_mass):
    peptide_vector = [0] * linear_spectrum(peptide_string, AA_mass)[-1]

    prefix_mass = 0
    for AA in peptide_string:

        prefix_mass = prefix_mass + AA_mass[AA]
        peptide_vector[prefix_mass - 1] = 1

    return(peptide_vector)


if __name__ == "__main__":
    peptide_string = 'NADA'
    # with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\peptidetovector.txt", 'r') as input_file:
    #     peptide_string = input_file.read()
    peptide_vector = peptide_to_vector(peptide_string, AA_mass)
    peptide_vector = list(map(str, peptide_vector))

    print(' '.join(peptide_vector))
