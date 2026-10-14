class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## keep track of last time seen a character
        ## need to keep track of left side

        seen = {}
        left = 0
        maxLength = 0

        for i in range(len(s)):
            if s[i] in seen:
                left = max(seen[s[i]] + 1, left) 
            seen[s[i]] = i
            maxLength = max(i - left + 1, maxLength)

        return maxLength
