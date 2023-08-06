arr=[4,7,8,1,2]
n=len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

for i in range(len(arr)):
    print(arr[i])