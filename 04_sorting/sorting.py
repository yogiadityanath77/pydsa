# Test arrays
arr = [5, 2, 4, 1]
arr1 = [5, 2, 4, 1, 2]
arr2 = [5, 2, 4, 1, 3]

def bubble_sort(arr):
    arr = arr.copy()
    for pass_num in range(len(arr) - 1):
        swapped = False
        for i in range(len(arr) - 1 - pass_num):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
    print("Bubble Sort Result:", arr)

def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print("Selection Sort Result:", arr)

def insertion_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print("Insertion Sort Result:", arr)

def main():
    print("=== Bubble Sort ===")
    bubble_sort(arr)

    print("\n=== Selection Sort ===")
    selection_sort(arr1)

    print("\n=== Insertion Sort ===")
    insertion_sort(arr2)

if __name__ == "__main__":
    main()