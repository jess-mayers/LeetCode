from typing import List

"""
You are given an integer array nums and an integer k. You may partition nums into one or more subsequences such that each element in nums appears in exactly one of the subsequences.
Return the minimum number of subsequences needed such that the difference between the maximum and minimum values in each subsequence is at most k.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
"""

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        result = 1
        nums.sort()
        min_val = nums[0]
        for num in nums[1:]:
            if num - min_val > k:
                result += 1
                min_val = num
        return result



if __name__ == '__main__':
    from utils import validate
    s = Solution()
    # result, expected
    validate(s.partitionArray([2, 0], 1), 2)
    validate(s.partitionArray([3,3,6,1,2,5], 2), 2)
    validate(s.partitionArray([3,6,1,2,5], 2), 2)
    validate(s.partitionArray([1,2,3], 1), 2)
    validate(s.partitionArray([2,2,4,5], 0), 3)