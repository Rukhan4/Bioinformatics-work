# String Reconstruction From Read Pairs Problem - returns a Text with (k,d)-mer composition equal to PairedRead

from EulerianPath import EulerianPath


with open('C:/Users/18687/Desktop/Bio Informatics/Bioinformatics specialization/quizQ3.txt') as input_data:
    k = 3
    paired_reads = [line.strip().split('|') for line in input_data.readlines()]
    d = 1


def StringReconstructionFromReadPairs(k, d, paired_reads):
    # Construct a dictionary of edges from the paired reads.
    paired_dict = {}
    for pair in paired_reads:
        if (pair[0][:-1], pair[1][:-1]) in paired_dict:
            paired_dict[(pair[0][:-1], pair[1][:-1])].append((pair[0][1:], pair[1][1:]))
        else:
            paired_dict[(pair[0][:-1], pair[1][:-1])] = [(pair[0][1:], pair[1][1:])]

    # Get an eulerian path from the paired edges.
    paired_path = EulerianPath(paired_dict)

    # Recombine the paths, accounting for their overlaps.
    strings = [paired_path[0][i] +
               ''.join(map(lambda x: x[i][-1], paired_path[1:])) for i in range(2)]
    text = strings[0][:k+d]+strings[1]
    return text


# Print and save the answer.
print(StringReconstructionFromReadPairs(k, d, paired_reads))
with open('C:/Users/18687/Desktop/Bio Informatics/Bioinformatics specialization/quiz3Answer.txt', 'w') as output_data:
    output_data.write(StringReconstructionFromReadPairs(k, d, paired_reads))
