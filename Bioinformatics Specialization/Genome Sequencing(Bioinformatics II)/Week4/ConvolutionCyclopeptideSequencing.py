# ConvolutionCyclopeptideSequencing - returns A cyclic peptide LeaderPeptide with amino acids
# taken only from the top M elements (and ties) of the convolution of Spectrum that
# fall between 57 and 200, and where the size of Leaderboard is restricted to the top N (and ties).

from SpectrumConvolution import SpectralConvolution
from LeaderboardCyclopeptideSequencing import LeaderboardCyclopeptideSequencing

integer_mass_table = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99,
                      'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
                      'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
                      'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}


def counted_convolution(spectrum):
    convolution = SpectralConvolution(spectrum)
    counted = {}
    for d in convolution:
        if 57 <= d <= 200:
            if counted.get(d):
                counted[d] += 1
            else:
                counted[d] = 1
    counted = [(k, v) for k, v in sorted(counted.items(), key=lambda item: item[1], reverse=True)]
    return counted


def convolution_cyclopeptide_sequencing(m, n, spectrum, amino_list=integer_mass_table):
    counted = counted_convolution(spectrum)
    convolution = [t[0] for i, t in enumerate(counted) if i < m]
    for t in counted[m:]:
        if t[1] == counted[m - 1][1]:
            convolution.append(t[0])
    reduced_amino = {k: v for k, v in amino_list.items() if v in convolution}
    x = LeaderboardCyclopeptideSequencing(spectrum, n, amino_list=reduced_amino)
    return PeptideToMass(x, amino_list=None)


def PeptideToMass(peptide, amino_list=None):
    """
    given a peptide string, return equivalent masses separated by -
    """

    if not amino_list:
        amino_list = integer_mass_table
    num = []
    for amino in peptide:
        num.append(str(amino_list[amino]))
    return '-'.join(num)


n = 20
m = 60
spectrum = "57 57 71 99 129 137 170 186 194 208 228 265 285 299 307 323 356 364 394 422 493"
formatspectrum = [int(x) for x in spectrum.split()]

print(convolution_cyclopeptide_sequencing(m, n, formatspectrum, amino_list=integer_mass_table))
