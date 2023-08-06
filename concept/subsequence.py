def find_subsequences(sequence):
    if len(sequence) == 0:
        return [[]]

    subseq = find_subsequences(sequence[1:])
    return subseq + [[sequence[0]] + sub for sub in subseq]

# Example usage:
sequence = [1, 2, 3]
subsequences = find_subsequences(sequence)
print(subsequences)
