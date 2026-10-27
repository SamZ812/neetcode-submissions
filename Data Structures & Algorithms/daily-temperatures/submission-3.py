class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)

        stack = []

        for index, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                topIndex = stack[-1][0]
                result[topIndex] = index - stack.pop()[0]
            stack.append([index, temperature])
        return result