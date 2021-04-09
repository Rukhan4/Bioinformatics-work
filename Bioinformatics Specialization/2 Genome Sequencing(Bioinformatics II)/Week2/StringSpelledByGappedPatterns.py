"""
StringSpelledByGappedPatterns.
     Input: Integers k and d followed by a sequence of (k, d)-mers (a1|b1), … , (an|bn) such that Suffix(ai|bi) = Prefix(ai+1|bi+1) for 1 ≤ i ≤ n-1.
     Output: A string Text of length k + d + k + n - 1 such that the i-th (k, d)-mer in Text is equal to (ai|bi)  for 1 ≤ i ≤ n (if such a string
     exists).
"""
import sys


def ReadFile(file):
    with open(file) as f:
        numbers = f.readline().split()
        k = int(numbers[0])
        d = int(numbers[1])

        patterns = f.readlines()
        patterns = [p.strip().split('|') for p in patterns]
    return (k, d, patterns)


def GappedGenomePathString(k, d, patterns):
    string = patterns[0][0]
    for p in patterns[1:d+1]:
        string += p[0][-1]
    string += patterns[0][1]
    for p in patterns[1:]:
        string += p[1][-1]
    return string


if __name__ == "__main__":
    file = sys.argv[1]
    (k, d, patterns) = ReadFile(file)
    string = GappedGenomePathString(k, d, patterns)
    print(string)
