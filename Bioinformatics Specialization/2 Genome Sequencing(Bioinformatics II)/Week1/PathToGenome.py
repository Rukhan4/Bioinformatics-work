# Path to Genome - Input: A sequence path of k-mers Pattern1, … ,Patternn such that
# the last k - 1 symbols of Patterni are equal to the first k-1 symbols
# of Patterni+1 for 1 ≤ i ≤ n-1.
# Output: A string Text of length k+n-1 such that the i-th k-mer in Text is equal to Patterni (for 1 ≤ i ≤ n).

"""
genome = [
    "ACCGA",
    "CCGAA",
    "CGAAG",
    "GAAGC",
    "AAGCT"
]
"""
file = open("C:/Users/18687/Desktop/Bio Informatics/Bioinformatics specialization/pathtogenome.txt", mode="r")
genome = file.read().strip().splitlines()


def PathToGenome(path):
    string = path[0]
    string += "".join([x[-1] for x in path[1:]])
    return string


print(PathToGenome(path))
file.close()
