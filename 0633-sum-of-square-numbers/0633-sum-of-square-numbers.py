class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(math.sqrt(c))
        
        while i <= j:
            sm = i*i + j*j
            if sm == c:
                return True
            elif sm < c:
                i += 1
            else:
                j -= 1
        return False