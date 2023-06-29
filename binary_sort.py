#!/usr/bin/env python

"""
Binary Sorter

Sorts the given list using the binary sort algorithm.

Author: CireWire
Date: 06/29/2023


def binary_sort(arr):
    """
    Sorts the given list using the binary sort algorithm.

    Args:
        arr (list): The unsorted list of integers.

    Returns:
        list: The sorted list.

    """
    # Base case: if the list contains 1 or fewer elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle index to divide the list into two halves
    mid = len(arr) // 2

    # Recursively sort the left and right halves of the list
    left_half = binary_sort(arr[:mid])
    right_half = binary_sort(arr[mid:])

    # Merge the sorted halves back together
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.

    Args:
        left (list): The left half of the original list.
        right (list): The right half of the original list.

    Returns:
        list: The merged and sorted list.

    """
    merged = []

    # While both left and right lists have elements
    while left and right:
        # Compare the first elements of both lists
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    # Append any remaining elements from either list
    merged.extend(left)
    merged.extend(right)

    return merged


# Let's test the algorithm with an example list

unsorted_list = [42, 7, 15, 99, 3, 21, 77]
sorted_list = binary_sort(unsorted_list)

print("Behold, the magnificent sorted list:")
print(sorted_list)
