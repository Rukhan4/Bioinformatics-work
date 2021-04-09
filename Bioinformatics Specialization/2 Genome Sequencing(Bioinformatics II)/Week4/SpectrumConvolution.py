# Spectral Convolution - returns the list of elements in the convolution of a Spectrum (that is, all positive differences of masses in the spectrum)


def SpectralConvolution(spectrum):
    sortedspectrum = sorted(spectrum)
    convolution = []
    for m in sortedspectrum:
        for n in sortedspectrum:
            diff = m-n
            if diff > 0:
                convolution.append(diff)
    return sorted(convolution)


spectrum = "0 97 99 103 114 128 137 156 186 200 213 225 251 259 285 293 314 328 350 356 396 399 407 411 413 484 493 506 510 510 514 527 536 607 609 613 621 624 664 670 692 706 727 735 761 769 795 807 820 834 864 883 892 906 917 921 923 1020"
formatspectrum = [int(x) for x in spectrum.split()]
print(*SpectralConvolution(formatspectrum))

if __name__ == "__main__":
    SpectralConvolution(spectrum)
