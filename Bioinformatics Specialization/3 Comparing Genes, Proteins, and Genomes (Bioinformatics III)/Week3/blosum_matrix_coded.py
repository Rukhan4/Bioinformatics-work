def Blosum62():
    B62 = {}
    with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\Comparing Genes, Proteins and Genomes (Bioinformatics III)\BLOSUM62.txt", 'r') as file:
        AA = file.readline().strip().split('  ')
        arrays = []
        for _ in AA:
            array = list(file.readline().strip().split(' '))
            while '' in array:
                array.remove('')
            array = list(int(i) for i in array[1:])
            arrays.append(array)
    for i in range(len(AA)):
        for j in range(len(AA)):
            B62[(AA[i], AA[j])] = arrays[i][j]
    return B62
