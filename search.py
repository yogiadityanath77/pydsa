# Test arrays
arr = [1, 2, 3, 4, 5]
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 4, 4, 4, 6, 8]

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            print("target found at index : ", i)
            return
    print("target not found")

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    found = False

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            print("target found at index : ", mid)
            found = True
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if not found:
        print("target not found")

def binary_search_first_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    found = False
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            answer = mid
            right = mid - 1
            found = True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if found:
        print("first occurrence found at index : ", answer)
    else:
        print("target not found")

def binary_search_last_occurrence(arr, target):
    left = 0
    right = len(arr) - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target :
            answer = mid
            left = mid + 1

        elif arr[mid] < target:
            left = mid + 1  

        else:
            right = mid - 1 
    if answer != -1:
        print("last occurrence found at index : ", answer)
    else:
        print("target not found")

def lower_bound_binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    if answer != -1:
        print("lower bound found at index : ", answer)
    else:
        print("target not found")

def higher_bound_binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    if answer != -1:
        print("higher bound found at index : ", answer)
    else:
        print("target not found")


def main():
    print("=== Linear Search ===")
    linear_search(arr, 3)

    print("\n=== Binary Search ===")
    binary_search(arr1, 3)

    print("\n=== Binary Search First Occurrence ===")
    binary_search_first_occurrence(arr2, 4)

    print("\n=== Binary Search Last Occurrence ===")
    binary_search_last_occurrence(arr2, 4)

    print("\n=== Lower Bound Binary Search ===")
    lower_bound_binary_search(arr2, 4)

    print("\n=== Higher Bound Binary Search ===")
    higher_bound_binary_search(arr2, 4)

if __name__ == "__main__":
    main()

