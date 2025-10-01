"""
Time Complexity:
    Best Case: O(1)
    Average Case: O(log N)
    Worst Case: O(log N)
"""

def binary_search(l: list, target: int) -> int:
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if l[mid] < target:
            low = mid + 1
        elif l[mid] > target:
            high = mid - 1
        else:
            # match found
            return mid
    # not found
    return -1

def binary_search_recursion(l: list, target: int) -> int:
    def helper(low: int, high: int) -> int:
        if high >= low:
            mid = low + (high - low) // 2
            if l[mid] < target:
                return helper(low=mid + 1, high=high)
            elif l[mid] > target:
                return helper(low=low, high=mid - 1)
            else:
                # match found
                return mid
        else:
            return -1
    return helper(0, len(l) - 1)