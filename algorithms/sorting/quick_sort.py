"""
Time Complexity:
    Best Case: (Ω(n log n)), Occurs when the pivot element divides the array into two equal halves.
    Average Case (θ(n log n)), On average, the pivot divides the array into two parts, but not necessarily equal.
    Worst Case: (O(n²)), Occurs when the smallest or largest element is always chosen as the pivot (e.g., sorted arrays).
"""
def swap(l, i, j):
    l[i], l[j] = l[j], l[i]

def partition(l: list, low: int, high: int) -> int:
    pivot = l[high]
    i = low - 1
    for j in range(low, high):
        if l[j] < pivot:
            i += 1
            swap(l, i, j)
    swap(l, i + 1, high)
    return i + 1

def quick_sort(l: list, low: int = 0, high: int = None) -> list:
    if high is None:
        high = len(l) - 1

    if low < high:
        pi = partition(l, low, high)
        # recurse left
        quick_sort(l, low, pi - 1)
        # recurse right
        quick_sort(l, pi + 1, high)

    return l
