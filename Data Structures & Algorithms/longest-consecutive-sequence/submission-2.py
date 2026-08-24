class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        ans = 0

        for i in seen:
            if i - 1 not in seen:
                length = 1
                while i + length in seen:
                    length += 1
                ans = max(length, ans)
        return ans
