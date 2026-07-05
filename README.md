# MSCS532_Assignment1

Insertion Sort implemented in Python for MSCS 532 — Assignment 1.

Based on the Insertion Sort algorithm presented in Chapter 2 of
*Introduction to Algorithms* (Cormen, Leiserson, Rivest, & Stein, 4th ed.),
modified to sort the array in **monotonically decreasing** order.

## How to run

Requires Python 3.8+.

```
python insertion_sort.py
```

This runs a demo on the CLRS example array `[5, 2, 4, 6, 1, 3]` and then a
small test suite covering edge cases (empty array, single element,
duplicates, already-sorted input, and negative numbers).

## How it works

Insertion sort iterates through the array, taking each element (the *key*)
and inserting it into its correct position among the elements before it.
To produce decreasing order, elements **smaller** than the key are shifted
right (the CLRS version shifts elements greater than the key), so larger
values settle toward the front of the array.

- Time complexity: O(n²) worst/average case, O(n) best case (already sorted)
- Space complexity: O(1) — sorts in place

## Reference

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022).
*Introduction to Algorithms* (4th ed.). MIT Press.
