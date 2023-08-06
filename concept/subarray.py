def find_subarrays(array):
    subarrays = []
    for i in range(len(array)):
        for j in range(i, len(array)):
            subarrays.append(array[i:j+1])
    return subarrays

# Example usage:
array = [1, 2, 3]
subarrays = find_subarrays(array)
print(subarrays)
