""" 
Code Challenge: Implement BetterBWMatching.

Input: A string BWT(Text) followed by a collection of strings Patterns.
Output: A list of integers, where the i-th integer corresponds to the number of substring matches of the i-th member of Patterns in Text.
"""


def last_to_first(text, i):
    first = [x for x in range(len(text))]
    first = sorted(first, key=lambda x: text[x])

    idx = text.index('$')
    for _ in range(len(text)):
        before = idx
        idx = first[idx]
        if idx == i:
            return before


def Count(symbol, n, text):
    return text[:n].count(symbol)


def FirstOccurrence(text, symbol):
    # returns the first position of symbol in firstColumn
    return sorted(text).index(symbol)


def BetterBWMatching(LastColumn, Pattern):
    text = LastColumn

    top = 0
    bottom = len(LastColumn)-1

    while top <= bottom:
        if len(Pattern) != 0:  #
            symbol = Pattern[-1]
            Pattern = Pattern[:-1]

            tmp = LastColumn[top:bottom+1]

            if symbol in tmp:
                top = FirstOccurrence(text, symbol)+Count(symbol, top, LastColumn)
                bottom = FirstOccurrence(text, symbol)+Count(symbol, bottom+1, LastColumn)-1
            else:
                return 0

        else:
            return bottom - top+1


# LastColumn = "GGCGCCGC$TAGTCACACACGCCGTA"
# Patterns = ["ACC", "CCG", "CAG"]
# answer = []
# for pattern in Patterns:
#     answer.append(BetterBWMatching(LastColumn, pattern))
# print(" ".join(map(str, answer)))

if __name__ == "__main__":
    file = open(
        r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\betterBWmatching.txt").read()
    LastColumn = (file.split('\n')[0])
    Patterns = [tmp for tmp in file.split("\n")[1].split() if tmp != '']

    answer = []
    for pattern in Patterns:
        answer.append(BetterBWMatching(LastColumn, pattern))
    print(" ".join(map(str, answer)))
