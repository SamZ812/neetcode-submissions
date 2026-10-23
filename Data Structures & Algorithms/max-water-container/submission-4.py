class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmt = 0

        left, right = 0, len(heights) - 1

        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            maxAmt = max(area, maxAmt)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
        return maxAmt