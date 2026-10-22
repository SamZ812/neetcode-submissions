class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])

        ## find target row
        top = 0
        bottom = rows - 1

        while top <= bottom:
            middle = (top + bottom) // 2
            if target < matrix[middle][0]:
                bottom = middle - 1
            elif target > matrix[middle][-1]:
                top = middle + 1
            else:
                break
        
        if not(top <= bottom):
            return False

        row = (top + bottom) // 2

        left, right = 0, columns - 1
        while left <= right:
            middle = (left + right) // 2
            if target < matrix[row][middle]:
                right = middle - 1
            elif target > matrix[row][middle]:
                left = middle + 1
            else:
                return True

        return False