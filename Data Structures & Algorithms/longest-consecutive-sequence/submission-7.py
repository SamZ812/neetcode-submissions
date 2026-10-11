class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ans = 0

        numSet = set(nums)

        if not numSet:
            return 0

        for i in numSet:
            if i - 1 not in numSet:
                length = 1
                while i + length in numSet:
                    length += 1
                ans = max(ans, length)
        
        return ans
