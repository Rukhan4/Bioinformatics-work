# Number of subpeptides of linear peptide length 'n'

def CountSubpeptides(n):
    return int(n * (n+1)/2 + 1)


print(CountSubpeptides(17623))
