"""
CODE CHALLENGE: Construct the graph of a spectrum.
Given: A space-delimited list of integers Spectrum.
Return: Graph(Spectrum).
"""

mass_AA_table = open(
    r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\Molecular Evolution(Bioinformatics IV)\integer_mass_table.txt", 'r').read()
mass_AA_table = mass_AA_table.split('\n')

mass_AA = dict()
for line in mass_AA_table:
    line = line.split(' ')
    mass_AA[int(line[1])] = line[0]


def spectrum_to_graph(spectrum, mass_AA):
    if type(spectrum) == str:
        spectrum = spectrum.split(' ')
        spectrum.append(0)
        spectrum = list(map(int, spectrum))

    graph = dict()
    for mass1 in spectrum:
        for mass2 in spectrum:
            delta = mass1 - mass2
            if delta in mass_AA:
                if mass2 in graph:
                    graph[mass2][mass1] = mass_AA[delta]
                else:
                    graph[mass2] = {mass1: mass_AA[delta]}
    return(graph)


if __name__ == "__main__":
    #spectrum = '57 71 154 185 301 332 415 429 486'

    with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\spectrumtograph.txt", "r") as input_file:
        spectrum = input_file.read()
    graph = spectrum_to_graph(spectrum, mass_AA)

    for key1, values1 in graph.items():
        for key2, value2 in values1.items():
            print(str(key1) + '->' + str(key2) + ':' + value2)
