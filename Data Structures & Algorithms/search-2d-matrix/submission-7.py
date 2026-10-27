class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])

        top, bottom = 0, rows - 1

        while top <= bottom:
            row = (top + bottom) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
            
        if not top <= bottom:
            return False

        left, right = 0, columns - 1

        while left <= right:
            middle = (left + right) // 2

            if matrix[row][middle] < target:
                left = middle + 1
            elif matrix[row][middle] > target:
                right = middle - 1
            else:
                return True
        return False