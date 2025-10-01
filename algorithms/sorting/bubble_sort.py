"""
    Time Complexity: O(n²)
"""
def bubble_sort(l: list) -> list:
    n = len(l)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                # swap elements
                l[j], l[j+1] = l[j+1], l[j]
                swapped = True
        if not swapped:
            break
    return l

"""
    Time Complexity: O(n²)
"""
def bubble_sort_recursion(l: list) -> list:
    def helper(n: int):
        swapped = False
        if n == 1:
            return
        for i in range(n):
            if l[i] > l[i+1]:
                # swap elements
                l[i], l[i + 1] = l[i + 1], l[i]
                swapped = True
        if not swapped:
            return
        # recurse
        helper(n - 1)
    helper(len(l) - 1)
    return l