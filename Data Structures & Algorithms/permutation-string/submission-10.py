class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        targetCounts = defaultdict(int)
        currCounts = defaultdict(int)

        for i in range(len(s1)):
            targetCounts[s1[i]] += 1
            currCounts[s2[i]] += 1

        if targetCounts == currCounts:
            return True

        left, right = 0, len(s1) - 1

        while right < len(s2) - 1:
            if currCounts[s2[left]] <= 1:
                del currCounts[s2[left]]
            else:
                currCounts[s2[left]] -= 1
            left += 1
            right += 1
            currCounts[s2[right]] += 1
            if targetCounts == currCounts:
                return True

        return False
            

        