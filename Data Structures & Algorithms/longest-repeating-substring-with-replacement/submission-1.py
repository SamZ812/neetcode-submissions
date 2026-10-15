class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxfrequency = 0
        result = 0

        counts = {}

        for right in range(len(s)):
            counts[s[right]] = 1 + counts.get(s[right], 0)
            maxfrequency = max(maxfrequency, counts[s[right]])

            while (right - left + 1) - maxfrequency > k:
                counts[s[left]] -= 1
                left += 1
            
            result = max(result, right - left  + 1)
        return result