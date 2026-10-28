class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # minimum speed would be 1, maximum speed would be max of piles

        left, right = 1, max(piles)

        result = right

        while left <= right:
            k = (left + right) // 2
            totalTime = 0

            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                result = k
                right = k - 1
            else:
                left = k + 1
        return result