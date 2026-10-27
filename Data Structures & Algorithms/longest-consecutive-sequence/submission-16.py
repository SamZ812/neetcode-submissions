class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0

        seen = set(nums)

        for i in seen:
            if i - 1 not in seen:
                length = 1
                while i + length in seen:
                    length += 1
                maxLength = max(length, maxLength)
        return maxLength