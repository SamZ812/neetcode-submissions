class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_length = 0
        left = 0
        for i in range(len(s)):

            if s[i] in seen:
                left = max(seen[s[i]] + 1, left)
            length = i - left + 1
            max_length = max(length, max_length)
            seen[s[i]] = i
        return max_length