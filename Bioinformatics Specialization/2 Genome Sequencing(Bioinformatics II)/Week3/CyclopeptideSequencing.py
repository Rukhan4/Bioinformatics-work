from CycloSpectrum import CycloSpectrum

integer_mass_table = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99,
                      'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
                      'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
                      'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}


def PrefixMaxArray(peptide, amino_list=None):
    if amino_list is None:
        amino_list = integer_mass_table
    prefix_max = [0]
    for i, letter in enumerate(peptide):
        prefix_max.append(prefix_max[i] + amino_list[letter])
    # print(prefix_max)
    return prefix_max


def LinearSpectrum(peptide, amino_list=None):
    prefix_max = PrefixMaxArray(peptide, amino_list=amino_list)
    LinearSpectrums = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            LinearSpectrums.append(prefix_max[j] - prefix_max[i])
    return sorted(LinearSpectrums)


def PeptideToMass(peptide, amino_list=None):
    if not amino_list:
        amino_list = integer_mass_table

    # given a peptide string, return equivalent masses separated by -

    num = []
    for amino in peptide:

        num.append(str(amino_list[amino]))
    return '-'.join(num)


def mass(peptide, amino_list=None):
    m = 0
    for amino_acid in peptide:
        m += integer_mass_table[amino_acid] if not amino_list else amino_list[amino_acid]
    return m


def Expand(peptides, amino_list=None):
    new_peptides = []
    for peptide in peptides:
        for amino_acid, _ in integer_mass_table.items() if not amino_list else amino_list.items():
            new_peptides.append(peptide + amino_acid)
    return new_peptides


def CyclopeptideSequencing(spectrum, amino_list=None):
    """
    :param spectrum: spectrum (list of int)
    :return: list of integers (amino acids)
    """
    parent_mass = max(spectrum)
    candidate_peptides = [""]
    final_peptides = []
    final_peptides_masses = []
    while len(candidate_peptides) > 0:
        candidate_peptides = Expand(candidate_peptides, amino_list=amino_list)
        for peptide in candidate_peptides[:]:
            if mass(peptide, amino_list=amino_list) == parent_mass and peptide not in final_peptides:
                if CycloSpectrum(peptide) == spectrum:
                    final_peptides.append(peptide)
                    final_peptides_masses.append(PeptideToMass(peptide, amino_list=amino_list))
                candidate_peptides.remove(peptide)
            elif not all(a in spectrum for a in LinearSpectrum(peptide, amino_list=amino_list)):
                candidate_peptides.remove(peptide)
    return set(final_peptides_masses)


print(*CyclopeptideSequencing([int(x) for x in "0 97 101 103 114 131 137 137 137 163 200 228 238 238 240 245 274 277 300 331 337 342 375 375 377 401 408 414 445 468 474 478 505 512 515 538 545 575 582 605 608 615 642 646 652 675 706 712 719 743 745 745 778 783 789 820 843 846 875 880 882 882 892 920 957 983 983 983 989 1006 1017 1019 1023 1120".split()]))
