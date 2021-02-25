# LeaderboardCyclopeptideSequencing.
# Input: An integer N and a collection of integers Spectrum.
# Output: LeaderPeptide after running LeaderboardCyclopeptideSequencing(Spectrum, N).


from collections import Counter

integer_mass_table = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99,
                      'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
                      'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
                      'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}


def LeaderboardCyclopeptideSequencing(spectrum, n, amino_list=None):
    count_ = []
    leaderboard = [""]
    leader_peptide = ""
    parent_mass = max(spectrum)
    leader_score = 0
    while len(leaderboard) > 0:
        leaderboard = Expand(leaderboard, amino_list=amino_list)
        for peptide in leaderboard[:]:
            mass_peptide = Mass(peptide, amino_list=amino_list)
            score_peptide = None
            if mass_peptide == parent_mass:
                score_peptide = CyclopeptideScore(peptide, spectrum)
                if score_peptide > leader_score:
                    leader_peptide = peptide
                    leader_score = score_peptide
            elif mass_peptide > parent_mass:
                leaderboard.remove(peptide)
            if (score_peptide and score_peptide == 83) or (CyclopeptideScore(peptide, spectrum, amino_list=amino_list) == 83):
                count_.append(PeptideToMass(peptide, amino_list=amino_list))
        leaderboard = Trim(leaderboard, spectrum, n, amino_list=amino_list)
    return PeptideToMass(leader_peptide, amino_list=amino_list)


def CyclopeptideScore(peptide, spectrum, amino_list=None):
    # Counter returns a dictionary

    theoretical_spectrum = CycloSpectrum(peptide)
    theoretical_counter = Counter(theoretical_spectrum)
    experimental_counter = Counter(spectrum)
    common_counter = theoretical_counter & experimental_counter
    # since Counter returns a dictionary we may add up the occurrences of the theoretical and experimental spectra values
    return sum(common_counter.values())


def CycloSpectrum(peptide):
    prefix_mass = [0]
    for amino_acid in peptide:
        prefix_mass.append(prefix_mass[-1] + integer_mass_table[amino_acid])

    peptide_mass = prefix_mass[-1]
    spectrum = [0]  # Instantiated with 0
    for i in range(len(peptide)):
        for j in range(1, len(peptide)+1):
            if i == j:
                continue
            elif j > i:
                spectrum.append(prefix_mass[j] - prefix_mass[i])
            else:
                spectrum.append(peptide_mass + prefix_mass[j] - prefix_mass[i])
    return sorted(spectrum)


def Mass(peptide, amino_list=None):
    """ 
    Retrieves mass from the integer mass table
    """

    m = 0
    for amino_acid in peptide:
        m += integer_mass_table[amino_acid] if not amino_list else amino_list[amino_acid]
    return m


def Expand(peptides, amino_list=None):
    """
    adds on a new amino acid to the current peptide
    """

    new_peptides = []
    for peptide in peptides:
        for amino_acid, _ in integer_mass_table.items() if not amino_list else amino_list.items():
            new_peptides.append(peptide + amino_acid)
    return new_peptides


def PrefixMaxArray(peptide, amino_list=None):
    if amino_list is None:
        amino_list = integer_mass_table
    prefix_max = [0]
    for i, letter in enumerate(peptide):
        prefix_max.append(prefix_max[i] + amino_list[letter])
    return prefix_max


def LinearSpectrum(peptide, amino_list=None):
    """
     returns the linear spectrum of an amino acid string peptide given that
      we have a dictionary amino acid mass whose keys are the symbols of alphabet of amino acids
      and whose values are the integer masses of each symbol
    """

    prefix_max = PrefixMaxArray(peptide, amino_list=amino_list)
    LinearSpectrums = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            LinearSpectrums.append(prefix_max[j] - prefix_max[i])
    return sorted(LinearSpectrums)


def LinearScore(peptide, spectrum, amino_list=None):
    """
    returns the count of the number of matches between linear spectrum of peptide and spectrum
    """

    s = spectrum.copy()
    count = 0
    for x in LinearSpectrum(peptide, amino_list=amino_list):
        if x in s:
            count += 1
            s.remove(x)
    return count


def Trim(leaderboard, spectrum, n, amino_list=None):
    """
    :param leaderboard: list of peptides
    :param spectrum: the spectrum wanted
    :param n: the array length (ties included)
    :return: collection of the top N highest-scoring linear peptides in Leaderboard (including ties) with respect to Spectrum.
    """

    Scores = []
    for i in range(len(leaderboard)):
        Scores.append(LinearScore(leaderboard[i], spectrum, amino_list))
    leaderboard = [x for _, x in sorted(zip(Scores, leaderboard))]
    leaderboard.reverse()
    Scores.sort()
    Scores.reverse()
    SuperLeader = leaderboard[0:n]
    for j in range(n, len(leaderboard)):
        if Scores[j] < Scores[j-1]:
            return (SuperLeader)
        else:
            SuperLeader.append(leaderboard[j])


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


spectrum = [int(x) for x in "0 71 99 101 113 114 114 114 114 114 115 128 128 128 128 128 129 147 156 156 156 163 199 200 227 227 228 229 229 242 242 242 242 243 248 255 255 261 284 284 285 291 300 319 328 341 341 355 356 356 357 357 357 362 376 383 384 389 398 398 405 411 429 447 447 447 455 455 469 469 471 471 484 485 490 490 497 513 518 539 540 545 561 561 561 575 576 583 583 583 584 585 585 599 611 612 618 632 641 646 653 668 674 684 689 689 689 690 698 698 708 711 713 732 739 739 740 746 755 768 774 782 788 802 803 809 812 818 826 826 831 836 840 845 846 853 854 867 869 874 896 897 902 916 916 937 937 940 940 945 950 968 968 968 974 974 981 982 987 989 1008 1010 1025 1030 1030 1030 1051 1063 1065 1068 1073 1081 1082 1096 1096 1096 1101 1103 1115 1124 1130 1136 1137 1139 1144 1145 1158 1164 1177 1179 1195 1197 1210 1224 1224 1229 1229 1229 1229 1231 1237 1250 1253 1259 1265 1272 1273 1278 1291 1292 1293 1323 1325 1338 1343 1344 1351 1357 1363 1366 1379 1385 1387 1387 1387 1387 1392 1392 1406 1419 1421 1437 1439 1452 1458 1471 1472 1477 1479 1480 1486 1492 1501 1513 1515 1520 1520 1520 1534 1535 1543 1548 1551 1553 1565 1586 1586 1586 1591 1606 1608 1627 1629 1634 1635 1642 1642 1648 1648 1648 1666 1671 1676 1676 1679 1679 1700 1700 1714 1719 1720 1742 1747 1749 1762 1763 1770 1771 1776 1780 1785 1790 1790 1798 1804 1807 1813 1814 1828 1834 1842 1848 1861 1870 1876 1877 1877 1884 1903 1905 1908 1918 1918 1926 1927 1927 1927 1932 1942 1948 1963 1970 1975 1984 1998 2004 2005 2017 2031 2031 2032 2033 2033 2033 2040 2041 2055 2055 2055 2071 2076 2077 2098 2103 2119 2126 2126 2131 2132 2145 2145 2147 2147 2161 2161 2169 2169 2169 2187 2205 2211 2218 2218 2227 2232 2233 2240 2254 2259 2259 2259 2260 2260 2261 2275 2275 2288 2297 2316 2325 2331 2332 2332 2355 2361 2361 2368 2373 2374 2374 2374 2374 2387 2387 2388 2389 2389 2416 2417 2453 2460 2460 2460 2469 2487 2488 2488 2488 2488 2488 2501 2502 2502 2502 2502 2502 2503 2515 2517 2545 2616".split()]
n = 211

print(LeaderboardCyclopeptideSequencing(spectrum, n, amino_list=None))

if __name__ == "__main__":
    LeaderboardCyclopeptideSequencing(spectrum, n)
