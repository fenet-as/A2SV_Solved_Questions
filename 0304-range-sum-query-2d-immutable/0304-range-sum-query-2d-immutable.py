class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0]*len(matrix[0]) for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                top = 0 if i-1 < 0 else self.prefix[i-1][j]
                left = 0 if j-1 < 0 else self.prefix[i][j-1]
                common = 0
                if j-1 >= 0 and i-1 >= 0:
                    common = self.prefix[i-1][j-1]
                self.prefix[i][j] = top + left - common + matrix[i][j]
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        whole = self.prefix[row2][col2]
        top = 0 if row1-1 < 0 else self.prefix[row1-1][col2]
        left = 0 if col1-1 < 0 else self.prefix[row2][col1-1]
        common = 0
        if row1-1 >= 0 and col1-1 >= 0:
            common = self.prefix[row1-1][col1-1]
        return whole - top - left + common
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)