amino_acid_mass = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99,
                   'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
                   'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
                   'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}

peptide = "ALTM"


def CycloSpectrum(peptide):
    prefix_mass = [0]
    for amino_acid in peptide:
        prefix_mass.append(prefix_mass[-1] + amino_acid_mass[amino_acid])

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


if __name__ == "__main__":
    print(*CycloSpectrum(peptide))
