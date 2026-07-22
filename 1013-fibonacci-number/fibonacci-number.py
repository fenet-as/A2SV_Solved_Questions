class Solution:
    def fib(self, n: int) -> int:
        


        def fibo(n,cache):
            if n < 2:
                return n

            if n in cache:
                return cache[n]
            cache[n] = fibo(n-1,cache) + fibo(n-2,cache)
            return cache[n]

        return fibo(n,{})

