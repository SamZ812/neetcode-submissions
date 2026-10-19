class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}

        length, maxLength, left = 0, 0, 0

        for i in range(len(s)):
            length += 1
            if s[i] in seen:
                left = max(left, seen[s[i]] + 1)
                length = i - left + 1
            seen[s[i]] = i
            maxLength = max(maxLength, length)
        return maxLength