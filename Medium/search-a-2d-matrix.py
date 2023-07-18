class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        begin = 0
        num_row = len(matrix)
        num_col = len(matrix[0])
        end = num_row * num_col - 1
        while begin <= end:
            mid = begin + (end - begin) // 2
            row = mid // num_col
            col = mid % num_col
            if matrix[row][col] > target:
                end = mid - 1
            elif matrix[row][col] < target:
                begin = mid + 1
            else:
                return True
        return False
