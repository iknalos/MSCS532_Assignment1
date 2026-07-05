"""Insertion Sort — MSCS 532 Assignment 1.

Based on the algorithm in Chapter 2 of Introduction to Algorithms
(Cormen, Leiserson, Rivest, & Stein, 4th ed.).
"""


def insertion_sort(arr):
    """Sort the list in place using insertion sort, in monotonically
    decreasing order.

    The comparison arr[j] < key (instead of arr[j] > key in CLRS)
    places larger elements first.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Shift elements smaller than key one position to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    data = [5, 2, 4, 6, 1, 3]
    print("Original array:", data)
    insertion_sort(data)
    print("Sorted array:  ", data)
