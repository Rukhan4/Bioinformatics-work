# Output Longest Common Subsequence Problem -
# Input: Two strings s and t.
# Output: A longest common subsequence of s and t'

import numpy as np
import sys

sys.setrecursionlimit(1500)  # necessary to bypass recursion limit


def lcs_backtrack(v, w):
    backtrack = [[""] * (len(w)) for _ in range(len(v))]
    s = np.zeros((len(v) + 1, len(w) + 1), dtype=int)
    for i in range(1, len(v) + 1):
        for j in range(1, len(w) + 1):
            match = 0
            if v[i - 1] == w[j - 1]:
                match = 1
            s[i][j] = max(s[i - 1][j], s[i][j - 1], s[i - 1][j - 1] + match)
            if s[i][j] == s[i - 1][j]:
                backtrack[i-1][j-1] = "↓"
            elif s[i][j] == s[i][j - 1]:
                backtrack[i-1][j-1] = "→"
            elif s[i][j] == s[i - 1][j - 1] + match:
                backtrack[i-1][j-1] = "↘"
    # print(s)
    # print(backtrack)
    return backtrack


def output_lcs(backtrack, v, i, j):
    if i == 0 or j == 0:
        return ""
    if backtrack[i-1][j-1] == "↓":  # down
        return output_lcs(backtrack, v, i - 1, j)
    elif backtrack[i-1][j-1] == "→":  # right
        return output_lcs(backtrack, v, i, j - 1)
    else:
        return output_lcs(backtrack, v, i - 1, j - 1) + v[i - 1]


def longest_common_subsequence(s, t):
    backtrack = lcs_backtrack(s, t)
    return output_lcs(backtrack, s, len(s), len(t))


#print(longest_common_subsequence("AACCTTGG", "ACACTGTGA"))

with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\outputlcs.txt", "r") as f:
    s = f.readline().rstrip()  # .rstrip() avoids the \n at the end of the line
    # or then do s = s.replace('\n','')
    t = f.readline().rstrip()
    print(longest_common_subsequence(s, t))
