class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []

        maxAmount = 0

        for i in prices:
            if stack:
                if stack[-1] < i:
                    maxAmount = max(maxAmount, i - stack[-1])
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return maxAmount

        