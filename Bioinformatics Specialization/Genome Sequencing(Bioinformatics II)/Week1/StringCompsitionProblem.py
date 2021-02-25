# String Composition Problem - Return the kmer composition of a string, Text, which is the
# collection of all kmer substrings of Text (including repeats)

""" 
Text = "CAATCCAAC"
k = 5
"""


def StringCompositionProblem(Text, k):
    kmer = []
    for i in range(len(Text)-k+1):
        kmer.append(Text[i:i+k])
    return kmer


file = open(
    "C:/Users/18687/Desktop/Bio Informatics/Bioinformatics specialization/datasetstringcomp.txt", mode="r")
f = file.read().strip().splitlines()
k = int(f[0])
Text = f[1]
#print('\n'.join(StringCompositionProblem(Text, k)))
file.close()

txt = '\n'.join(StringCompositionProblem(Text, k))
file = open(
    "C:/Users/18687/Desktop/Bio Informatics/Bioinformatics specialization/datasetstringcomp.txt", mode="w")
file.write(txt)
file.close()
