# Paired Composition Problem - Given integers k, d and a DNA string Text, return
# the composition of k,d-mers that make up Text. Output will be in lexicographical order

def PairedComposition(k, d, Text):
    composition = []
    for i in range(len(Text)):
        start_0 = i
        end_0 = start_0+k
        start_1 = i+k+d
        end_1 = start_1 + k
        if end_1 <= len(Text):
            kmer_0 = Text[start_0:end_0]
            kmer_1 = Text[start_1:end_1]
            composition.append([kmer_0, kmer_1])
        else:
            break
    return sorted(composition)


comp = PairedComposition(3, 2, "TAATGCCATGGGATGTT")
for pair in comp:
    print('(' + pair[0] + '|' + pair[1] + ')', end=' ')

with open('C:/Users/18687/Desktop/Bio Informatics/Bioinformatics specialization/composition.txt', 'w') as file:
    for pair in comp:
        file.write('(' + str(list[0]) + '|' + str(list[1]) + ')')
file.close()
