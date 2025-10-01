import random
def is_sorted(l) -> bool:
    n = len(l)
    for i in range(0, n-1):
        if l[i] > l[i + 1]:
            return False
    return True
"""
Time Complexity: 
    Worst Case : O(inf) (since this algorithm has no upper bound)
    Average Case: O(n*n!)
    Best Case : O(n)(when array given is already sorted)
"""
def bogo_sort(l: list) -> list:
    while not is_sorted(l):
        random.shuffle(l)
    return l