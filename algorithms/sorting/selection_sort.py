"""
Time Complexity: O(n²)
"""
def selection_sort(l: list) -> list:
    n = len(l)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if l[j] < l[min_idx]:
                min_idx = j
        l[i], l[min_idx] = l[min_idx], l[i]
    return l
