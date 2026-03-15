class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        

        m = 0
        ct = 0
        while m < maxDoubles and target > 1:
            if target % 2 == 1:
                target -= 1
                ct += 1
                continue

            elif target // 2 >= 1:
                ct += 1
                target //= 2
            m += 1
        if target > 1:
            ct += (target - 1)
        return ct
        
