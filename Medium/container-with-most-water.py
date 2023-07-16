class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return
        left = 0
        right = len(height) - 1
        max_area = 0
        h = max(height)
        while left < right:
            left_height = height[left]
            right_height = height[right]
            max_area = max(max_area, min(left_height, right_height) * (right - left))
            if left_height < right_height:
                left += 1
            elif right_height <= left_height:
                right -= 1
            if (right - left) * h <= max_area:
                break
        
        return max_area
