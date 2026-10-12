class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lookupLength = len(s1)

        if lookupLength > len(s2):
            return False

        counts = defaultdict(int)

        for i in s1:
            counts[i] += 1

        left, right = 0, lookupLength
        currentCounts = defaultdict(int)
        for i in range(lookupLength):
            currentCounts[s2[i]] += 1
        if counts == currentCounts:
                return True
        while right < len(s2):
            print(counts, currentCounts)
            if currentCounts[s2[left]] <= 1:
                del currentCounts[s2[left]]
            else:
                currentCounts[s2[left]] -= 1
            left += 1
            currentCounts[s2[right]] += 1
            right += 1
            if counts == currentCounts:
                return True
        return False

