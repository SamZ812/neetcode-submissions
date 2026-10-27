class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []

        maxProfit = 0

        for i in prices:
            if stack and stack[-1] < i:
                maxProfit = max(maxProfit, i - stack[-1])
            else:
                stack.append(i)
        return maxProfit