class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        curr = 0
        for i in nums:
            if i == 0:
                curr = 0
            else:
                curr += 1
                ans = max(ans, curr)
        return ans