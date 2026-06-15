# Bubble Sort

arr = [5,2,4,1]

for pass_num in range(len(arr)-1):
    swapped = False
    for i in range(len(arr)-1-pass_num):
        if arr[i]> arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
            swapped = True

        if not swapped:
            break
print(arr)