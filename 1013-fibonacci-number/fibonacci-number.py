class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        cache = [0,1]
        i = 2

        while i <= n:
            tm = cache[1]
            cache[1] = cache[1]+ cache[0]
            cache[0]=tm
            i += 1

        return cache[1]


