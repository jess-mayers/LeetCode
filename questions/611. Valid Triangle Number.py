from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # sort list for 2 pointer method
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n):
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    count += r - l
                    r -= 1
                else:
                    l += 1
        return count

if __name__ == '__main__':
    s = Solution()
    print(s.triangleNumber([2,2,3,4]), 3)
    print(s.triangleNumber([4,2,3,4]), 4)