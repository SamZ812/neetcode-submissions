class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxAmt = 0
        counts = defaultdict(int)
        maxLength = 0

        for right in range(len(s)):
            counts[s[right]] += 1
            maxAmt = max(maxAmt, counts[s[right]])
            if (right - left + 1) - maxAmt > k:
                counts[s[left]] -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength

