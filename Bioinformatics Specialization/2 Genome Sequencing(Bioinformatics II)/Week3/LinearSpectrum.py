# Linear Spectrum - returns the linear spectrum of an amino acid string peptide given that
# we have a dictionary amino acid mass whose keys are the symbols of alphabet of amino acids
# and whose values are the integer masses of each symbol


AminoAcidMass = {
    'G': 57,
    'A': 71,
    'S': 87,
    'P': 97,
    'V': 99,
    'T': 101,
    'C': 103,
    'I': 113,
    'L': 113,
    'N': 114,
    'D': 115,
    'K': 128,
    'Q': 128,
    'E': 129,
    'M': 131,
    'H': 137,
    'F': 147,
    'R': 156,
    'Y': 163,
    'W': 186
}

Peptide = "NQEL"


def LinearSpectrum(Peptide, AminoAcidMass):
    PrefixMass = [0]
    for aminoacid in Peptide:
        PrefixMass.append(PrefixMass[-1] + AminoAcidMass[aminoacid])

    LSpectrum = [0]
    for i in range(len(Peptide)):
        for j in range(i+1, len(Peptide)+1):
            LSpectrum.append(PrefixMass[j] - PrefixMass[i])

    return sorted(LSpectrum)


print(*LinearSpectrum(Peptide, AminoAcidMass))

""" 
def CyclicSpectrum(Peptide, AminoAcidMass):
    PrefixMass = [0]
    for aminoacid in Peptide:
        PrefixMass.append(PrefixMass[-1] + AminoAcidMass[aminoacid])
    peptideMass = PrefixMass(len(Peptide))

    CSpectrum = [0]
    for i in range(len(Peptide)):
        for j in range(i+1, len(Peptide)+1):
            CSpectrum.append(PrefixMass[j] - PrefixMass[i])
            if i>0 and j<len(Peptide):
                CSpectrum.append(peptideMass - (PrefixMass[j] - PrefixMass[i]))

    return sorted(CSpectrum)

"""
