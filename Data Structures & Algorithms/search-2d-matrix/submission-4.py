class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])

        # identify which row we have a target in
        top, bottom = 0, rows - 1

        while top <= bottom:
            row = (top + bottom) // 2

            if target < matrix[row][0]:
                bottom = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break

        # find the target in row we found

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