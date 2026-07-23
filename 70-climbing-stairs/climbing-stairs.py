class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(step):
            # Base case: reached the top
            if step == n:
                return 1

            # Base case: went beyond the top
            if step > n:
                return 0

            # Return cached result
            if step in memo:
                return memo[step]

            # Take either 1 step or 2 steps
            memo[step] = dp(step + 1) + dp(step + 2)

            return memo[step]

        return dp(0)