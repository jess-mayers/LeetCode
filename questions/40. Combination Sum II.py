from typing import List

class Solution:
    # ease of access of result
    result = None
    def helper(self, candidates: List[int], target: int, combination: list):
        if target < 0:
            return
        if target == 0:
            self.result.append(list(combination))
            return

        for i in range(len(candidates)):
            if candidates[i] > target:
                break
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            self.helper(candidates[i+1:], target-candidates[i], combination + [candidates[i]])

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # init
        self.result = []
        candidates.sort()
        self.helper(candidates, target, [])
        print(self.result)
        return self.result


if __name__ == '__main__':
    s = Solution()
    s.combinationSum2([10,1,2,7,6,1,5], 8) # [[1,1,6],[1,2,5],[1,7],[2,6]]
    s.combinationSum2([2,5,2,1,2], 5) # [[1,2,2],[5]]
    # s.combinationSum([2], 1)