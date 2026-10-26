class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # minimum eating = 1, maximum eating = max in one pile

        left, right = 1, max(piles)
        result = right

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
            
            
