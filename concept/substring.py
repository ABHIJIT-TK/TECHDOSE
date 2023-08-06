def find_substrings(string):
    substrings = []
    for i in range(len(string)):
        for j in range(i, len(string)):
            substrings.append(string[i:j+1])
    return substrings

# Example usage:
string = "abc"
substrings = find_substrings(string)
print(substrings)
