arr=[2,3,1,4]
for i in range(len(arr)):
    mini= i
    for j in range(i+1, len(arr)):
        if arr[mini] > arr[j]:
            mini = j
    arr[i], arr[mini] = arr[mini], arr[i]
for i in range(len(arr)):
    print(arr[i])
  