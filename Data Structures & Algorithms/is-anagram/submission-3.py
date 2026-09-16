class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCounts = defaultdict(int)
        tCounts = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            sCounts[s[i]] += 1
            tCounts[t[i]] += 1

        for x, y in sCounts.items():
            if tCounts[x] != y:
                return False
        return True