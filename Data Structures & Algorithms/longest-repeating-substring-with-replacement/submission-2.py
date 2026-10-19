class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxAmt = 0
        ans = 0

        seen = defaultdict(int)

        for right in range(len(s)):
            seen[s[right]] += 1 
            maxAmt = max(maxAmt,seen[s[right]])
            ## if window - max frequency > k, move window in
            if (right - left + 1) - maxAmt > k:
                seen[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
            
