class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        heights_num = len(heights)
        stack = []

        for i in range(heights_num):
            idx = i
            while stack and stack[-1][1] > heights[i]:
                removed_index, removed_height = stack.pop()
                curr_area = (i - removed_index) * removed_height
                if curr_area > max_area:
                    max_area = curr_area
                idx = removed_index
            stack.append((idx, heights[i]))
        while stack:
            index, height = stack.pop()
            area = (heights_num - index) * height
            if area > max_area:
                max_area = area
        return max_area
