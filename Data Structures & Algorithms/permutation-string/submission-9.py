class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        stringLength = len(s1)

        if stringLength > len(s2):
            return False

        targetCount = defaultdict(int)
        currentCount = defaultdict(int)

        for i in range(stringLength):
            targetCount[s1[i]] += 1
            currentCount[s2[i]] += 1

        if targetCount == currentCount:
            return True

        left, right = 0, stringLength - 1

        while right < len(s2) - 1:
            if currentCount[s2[left]] <= 1:
                del currentCount[s2[left]]
            else:
                currentCount[s2[left]] -= 1
            left += 1
            right += 1
            currentCount[s2[right]] += 1
            if targetCount == currentCount:
                return True
        return False
            