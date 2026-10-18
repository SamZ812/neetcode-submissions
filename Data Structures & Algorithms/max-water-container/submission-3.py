class Solution:
    def maxArea(self, heights: List[int]) -> int:
        currArea = 0
        maximumArea = 0

        left, right = 0, len(heights) - 1

        while left <= right:
            currArea = (right - left) * min(heights[left], heights[right])
            maximumArea = max(maximumArea, currArea)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maximumArea
    