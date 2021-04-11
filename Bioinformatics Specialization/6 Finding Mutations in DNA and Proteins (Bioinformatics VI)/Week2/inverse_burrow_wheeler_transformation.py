'''
Inverse Burrows-Wheeler Transform Problem: Reconstruct a string from its Burrows-Wheeler transform.
Input: A string Transform (with a single "$" symbol).
Output: The string BW_string such that BWT(text) = Transform.

Code Challenge: Solve the Inverse Burrows-Wheeler Transform Problem.
'''


def inverse_BWT(BW_string):
    len_txt = len(BW_string)
    last_col = [(BW_string[i], i) for i in range(len_txt)]
    first_col = sorted(last_col)
    original = [first_col[0]]
    for i in range(len_txt):
        original.append(first_col[last_col.index(original[i])])

    return ''.join(x[0] for x in original[1:])


BW_string = 'TTCCATTGGA$'
print(inverse_BWT(BW_string))


# if __name__ == "__main__":
#     with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\inverseBWT.txt", "r") as file:
#         BW_string = file.read().strip()

#     print(inverse_BWT(BW_string))
