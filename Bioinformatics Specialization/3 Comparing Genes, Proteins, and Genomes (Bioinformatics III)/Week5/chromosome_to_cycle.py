# Chromosome To Cycle
# Input: A chromosome Chromosome containing n synteny blocks.
# Output: The sequence Nodes of integers between 1 and 2n resulting from applying ChromosomeToCycle to Chromosome.

def chromosome_to_cycle(chromosome):
    if type(chromosome) == str:
        chromosome = chromosome.split(' ')
    chromosome = list(map(int, chromosome))

    nodes = []
    for old_node in chromosome:
        if old_node > 0:
            nodes.extend([2 * old_node - 1, 2 * old_node])
        else:
            nodes.extend([-2 * old_node, -2 * old_node - 1])
    return nodes


if __name__ == '__main__':
    chromosome = ("+1 +2 +3 +4 -5 +6 -7 +8 -9 -10 -11 -12 +13 +14 +15 +16 -17 +18 -19 +20 +21 -22 -23 +24 -25 -26 +27 +28 -29 +30 +31 +32 +33 +34 +35 -36 -37 +38 -39 -40 -41 +42 -43 +44 +45 +46 +47 +48 -49 +50 +51 -52 -53 -54 +55 +56 +57 +58 +59 +60 +61 -62 +63 +64 +65 +66")

    middle = (chromosome_to_cycle(chromosome))
    answer = tuple(middle)
    print(*answer)
