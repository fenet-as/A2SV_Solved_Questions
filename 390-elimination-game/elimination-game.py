class Solution:
    def lastRemaining(self, n: int) -> int:

        def helper(n,dir,step,head):
            if n == 1:
                return head

            if dir == 1:  # left to right
                head += step
            else:
                if n % 2 == 1:
                    head += step

            step *= 2
            n //= 2
            dir *= -1

            return helper(n,dir,step,head)

        return helper(n,1,1,1)
        


