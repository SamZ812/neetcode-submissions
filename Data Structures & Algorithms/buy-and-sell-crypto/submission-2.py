class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0

        stack = []

        ## use stack to input prices, (price, index).
        ## if price is higher than stack[-1], pop, take difference in index
        ## and update maxPro

        for i in prices:
            if stack and stack[-1] < i:
                currMax = i - stack[-1]
                maxPro = max(currMax, maxPro)
            else:
                stack.append(i)
        return maxPro