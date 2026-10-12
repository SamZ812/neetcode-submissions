class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0
        maxLength = 0
        for i in range(len(s)):
            if s[i] in seen and seen[s[i]] >= start:
                start = seen[s[i]] + 1
            seen[s[i]] = i
            maxLength = max(i - start + 1, maxLength)
        return maxLength