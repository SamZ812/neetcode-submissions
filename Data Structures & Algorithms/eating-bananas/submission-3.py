class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate = max(piles)

        left, right = 1, max_rate

        while left <= right:
            totalTime = 0
            k = (left + right) // 2

            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                result = k
                right = k - 1
            else:
                left = k + 1
        return result