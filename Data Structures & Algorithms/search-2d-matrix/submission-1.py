import math

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, (m*n) - 1
        if matrix[r // n][r % n] == target or matrix[l // n][l % n] == target:
            return True
        while r - 1 > l:
            mid = (r + l) // 2
            if matrix[mid // n][mid % n] > target:
                r = mid
            elif matrix[mid // n][mid % n] < target:
                l = mid
            else:
                return True
        return False
