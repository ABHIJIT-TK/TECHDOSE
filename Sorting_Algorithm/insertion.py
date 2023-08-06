arr=[9,8,7,6,5]
for i in range(1, len(arr)):

    val = arr[i]

    # Move elements of arr[0..i-1], that are
    # greater than val, to one position ahead
    # of their current position
    j = i-1
    while j >= 0 and val < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
    arr[j + 1] = val
for i in range(len(arr)):
    print(arr[i])