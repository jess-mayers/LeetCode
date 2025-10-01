"""
Time Complexity
    Best case: O(n), If the list is already sorted, where n is the number of elements in the list.
    Average case: O(n²), If the list is randomly ordered
    Worst case: O(n²), If the list is in reverse order
"""

def insertion_sort(l: list) -> list:
    for i in range(len(l)):
        k = l[i]
        j = i - 1
        while j >= 0 and k < l[j]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = k
    return l