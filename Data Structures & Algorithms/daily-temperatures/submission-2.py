class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack = []

        for index, temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                topIndex = stack[-1][1]
                result[topIndex] = index - stack.pop()[1]
            stack.append([temperature, index])
        return result