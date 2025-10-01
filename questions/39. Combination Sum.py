from typing import List

class Solution:
    # ease of access of result
    result = None
    def helper(self, candidates: List[int], target: int, combination: list = []):
        s = sum(combination)
        if s > target or not candidates:
            # when current sum is greater than target or no more candidates
            return
        elif s == target:
            # sum matches return
            self.result.append(list(combination))
            return

        candidate = candidates[0]
        combination.append(candidate)
        # check for the same value
        self.helper(candidates, target, combination)
        # pop since we are over target
        combination.pop()
        # move on to next value in candidates
        self.helper(candidates[1:], target, combination)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # init
        self.result = []
        # work backwards
        candidates.sort()
        self.helper(candidates, target, [])
        return self.result


if __name__ == '__main__':
    s = Solution()
    s.combinationSum([2,3,6,7], 7)
    # s.combinationSum([2,3,5], 8)
    # s.combinationSum([2], 1)