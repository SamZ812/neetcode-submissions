class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack = []

        for index, temp in enumerate(temperatures):
                while stack and temp > stack[-1][0]:
                    topIndex = stack[-1][1]
                    result[topIndex] = index - stack.pop()[1] 
                stack.append([temp, index])

        return result