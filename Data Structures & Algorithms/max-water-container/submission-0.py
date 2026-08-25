class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # keep track of the area: L x W L being heights[i] and W being the window
        # size (left - right + 1)

        left, right = 0, len(heights) - 1
        ans = 0
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            ans = max(ans, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return ans