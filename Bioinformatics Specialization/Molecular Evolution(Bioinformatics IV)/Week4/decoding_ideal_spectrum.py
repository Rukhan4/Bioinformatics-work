'''
CODE CHALLENGE: Solve the Decoding an Ideal Spectrum Problem.
Given: A space-delimited list of integers Spectrum.
Return: An amino acid string that explains Spectrum.
'''
from spectrum_to_graph import spectrum_to_graph

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


def linear_spectrum(peptide_string, AA_mass):
    prefix_weight = [0]
    for AA in peptide_string:
        prefix_weight.append(prefix_weight[-1] + AA_mass[AA])

    linear_spectrum = [0]
    for i in range(len(peptide_string)):
        for j in range(i + 1, len(peptide_string) + 1):
            linear_spectrum.append(prefix_weight[j] - prefix_weight[i])
    linear_spectrum.sort()
    return(linear_spectrum)


def decoding_ideal_spectrum(spectrum, mass_AA, AA_mass):
    if type(spectrum) == str:
        spectrum = spectrum.split(' ')
        spectrum = [0] + spectrum
        spectrum = list(map(int, spectrum))

    graph = spectrum_to_graph(spectrum, mass_AA)

    for start in graph.keys():
        peptide_string = ''
        find_graph_path(graph, start, peptide_string, spectrum)


def find_graph_path(graph, start, peptide_string, target_spectrum):

    current_spectrum = linear_spectrum(peptide_string, AA_mass)
    if current_spectrum[-1] == target_spectrum[-1]:

        check = 1

        for item in target_spectrum:
            if item not in current_spectrum:
                check = check * 0
                break
        if check == 1:
            print(peptide_string)

    if start in graph:
        mass2_graph = graph[start]
        for mass2, AA in mass2_graph.items():
            find_graph_path(graph, mass2, peptide_string + AA, target_spectrum)


if __name__ == "__main__":
    #spectrum = '57 71 154 185 301 332 415 429 486'

    with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\decodingidealspectrum.txt", "r") as input_file:
        spectrum = input_file.read()
    decoding_ideal_spectrum(spectrum, mass_AA, AA_mass)
