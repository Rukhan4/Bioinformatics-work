# Implement CycleToChromosome.
# Input: A sequence Nodes of integers between 1 and 2n.
# Output: The chromosome Chromosome containing n synteny blocks resulting from applying CycleToChromosome to Nodes.

def cycle_to_chromosome(nodes):
    if type(nodes) == str:
        nodes = nodes.split(' ')
    nodes = list(map(int, nodes))
    nodes = [0] + nodes

    chromosome = []

    for i in range(1, (int(len(nodes)/2) + 1)):
        if nodes[2 * i - 1] < nodes[2 * i]:
            node = int(nodes[2*i] / 2)
            positive = '+'
            node = f'{positive}{node}'
        else:
            node = int(-1 * nodes[(2*i) - 1] / 2)

        chromosome.append(node)

    return chromosome


if __name__ == "__main__":
    nodes = '1 2 3 4 5 6 8 7 9 10 12 11 13 14 16 15 18 17 19 20 21 22 23 24 26 25 27 28 30 29 32 31 34 33 35 36 37 38 40 39 41 42 43 44 45 46 48 47 50 49 51 52 53 54 56 55 58 57 59 60 61 62 64 63 65 66 68 67 70 69 72 71 74 73 75 76 77 78 80 79 81 82 84 83 85 86 87 88 89 90 91 92 93 94 96 95 97 98 99 100 101 102 103 104 106 105 107 108 109 110 111 112 114 113 116 115 118 117 119 120 121 122 123 124 125 126 128 127 129 130 132 131 133 134 135 136 138 137 140 139'

    answer = cycle_to_chromosome(nodes)
    print(*tuple(map(str, answer)))
    # print(tuple(answer))
