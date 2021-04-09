# Counting Peptides with Given Mass - returns the number of linear peptides having integer mass from a given mass 'm'
# Solve the Counting Peptides with Given Mass Problem.
# The integer mass table is reproduced below; recall that we assume that peptides are
# formed from only 18 amino acid masses.
# That is, I/L are considered the same and K/Q are considered the same,
# so we would count AIKD and ALQD as just one peptide, not two.

def CountingPeptidesWithGivenMass(m):
    mass_list = [57, 71, 87, 97, 99, 101, 103, 113, 114,
                 115, 128, 129, 131, 137, 147, 156, 163, 186]
    table = [0]*(m+1)  # Dynamic program method of tabulation
    table[0] = 1
    for i in range(1, m+1):
        for j in mass_list:
            if i-j >= 0:
                table[i] += table[i-j]
    return table[m]


print(CountingPeptidesWithGivenMass(1275))


""" 
for a large m, the no of peptides with given integer mass m can be approximated as kC^m where k and C are constants.
assuming k = 1: 

def calculate_c(num_1, num_2):
    i_1 = CountingPeptidesWithGivenMass(num_1)
    i_2 = CountingPeptidesWithGivenMass(num_2)

    c = exp(log(i_1 / i_2) / (num_1 - num_2))

    return

 

calculate_c(5000,2500)
"""
