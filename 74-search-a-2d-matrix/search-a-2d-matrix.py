class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        i = 0
        j = (m*n)-1

        while i <= j:
            mid = i+ (j-i)//2

            r = mid//n
            c = mid%n

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                i = mid+1
            else:
                j= mid-1
        return False
