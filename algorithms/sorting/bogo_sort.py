"""
Time Complexity:
    Worst Case : O(inf) - There is no end case. It can go on forever
    Average Case: O(n*n!)
    Best Case : O(n) - array is already sorted
"""

import random
def is_sorted(l) -> bool:
    n = len(l)
    for i in range(0, n-1):
        if l[i] > l[i + 1]:
            return False
    return True
def bogo_sort(l: list) -> list:
    while not is_sorted(l):
        random.shuffle(l)
    return l