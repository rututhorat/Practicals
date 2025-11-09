import random
import time

# -----------------------------
# Deterministic Quick Sort
# -----------------------------
def deterministic_partition(arr, low, high):
    pivot = arr[high]  # last element as pivot
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def deterministic_quick_sort(arr, low, high):
    if low < high:
        pi = deterministic_partition(arr, low, high)
        deterministic_quick_sort(arr, low, pi - 1)
        deterministic_quick_sort(arr, pi + 1, high)

# -----------------------------
# Randomized Quick Sort
# -----------------------------
def randomized_partition(arr, low, high):
    rand_pivot = random.randint(low, high)
    arr[high], arr[rand_pivot] = arr[rand_pivot], arr[high]
    return deterministic_partition(arr, low, high)

def randomized_quick_sort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)

# -----------------------------
# Analysis Function
# -----------------------------
def analyze_quick_sort():
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter elements separated by space: ").split()))

    print("\nOriginal Array:", arr)

    # Deterministic Quick Sort
    arr1 = arr.copy()
    start = time.time()
    deterministic_quick_sort(arr1, 0, n - 1)
    end = time.time()
    print("\nSorted Array (Deterministic Quick Sort):", arr1)
    print("Execution Time (Deterministic):", round(end - start, 6), "seconds")

    # Randomized Quick Sort
    arr2 = arr.copy()
    start = time.time()
    randomized_quick_sort(arr2, 0, n - 1)
    end = time.time()
    print("\nSorted Array (Randomized Quick Sort):", arr2)
    print("Execution Time (Randomized):", round(end - start, 6), "seconds")

if __name__ == "__main__":
    analyze_quick_sort()
