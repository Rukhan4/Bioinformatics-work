# Number of Breakpoints Problem: Find the number of breakpoints in a permutation.

# Input: A permutation.
# Output: The number of breakpoints in this permutation.


def breakpoints(permutation):
    # formatting
    if type(permutation) == str:
        permutation = permutation.split(' ')
    permutation = list(map(int, permutation))

    breakpoint_counter = 0

    permutation = [0] + permutation + [len(permutation) + 1]  # adding the 0 and (n+1) terms

    for i in range(len(permutation) - 1):  # not checking the immutable (n+1) term
        if permutation[i] != permutation[i+1] - 1:
            breakpoint_counter += 1

    return breakpoint_counter


with open(r"C:\Users\18687\Desktop\Bio Informatics\Bioinformatics specialization\testsets\breakpoints.txt", "r") as input_file:
    permutation = input_file.read()

print(breakpoints(permutation))
