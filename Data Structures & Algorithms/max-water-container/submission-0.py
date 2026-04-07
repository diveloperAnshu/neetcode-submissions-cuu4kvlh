class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = 0
        maxArea = 0
        while left <= right:
            if heights[left] <= heights[right]:
                area = (heights[left] * (right - left))
                maxArea = max(area, maxArea)
                left += 1
            else:
                area = heights[right] * (right - left)
                maxArea = max(area, maxArea)
                right -= 1
        return maxArea
            

        