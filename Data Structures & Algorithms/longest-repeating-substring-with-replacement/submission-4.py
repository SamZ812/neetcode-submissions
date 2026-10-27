class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)

        left = 0

        max_length = 0
        maxAmt = 0

        for right in range(len(s)):
            counts[s[right]] += 1
            maxAmt = max(maxAmt, counts[s[right]])
            if (right - left + 1) - maxAmt > k:
                counts[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length