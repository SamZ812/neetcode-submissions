class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1

        ## move left to the right if wall is lower than right, otherwise move right in
        maxArea = 0
        while left <= right:
            currArea = (right - left) * min(heights[left], heights[right])
            maxArea = max(maxArea, currArea)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxArea