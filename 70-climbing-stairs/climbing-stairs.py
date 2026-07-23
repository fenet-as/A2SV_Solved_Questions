class Solution:
    def climbStairs(self, n: int) -> int:
        
     

        def rec(c,n,memo):
            if c == n:
                return 1

            elif c > n:
                return 0
            
            if c in memo:
                return memo[c]

            memo[c] = rec(c+1,n,memo) + rec(c+2,n,memo)

            return memo[c]

        return rec(0,n,{})

