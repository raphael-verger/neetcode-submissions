from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u, d = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1

        while u <= d:
            mid_row = (u + d) // 2

            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                break
            elif matrix[mid_row][0] < target:
                u = mid_row + 1
            else:
                d = mid_row - 1
        else:
            return False

        while l <= r:
            mid = (l + r) // 2

            if matrix[mid_row][mid] == target:
                return True
            elif matrix[mid_row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
