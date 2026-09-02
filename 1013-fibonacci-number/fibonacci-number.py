class Solution:
    def fib(self, n: int) -> int:

        hashmap = {}

        def fb(n):

            if n == 0 or n == 1 :return n

            if n-1 not in hashmap: hashmap[n-1] = fb(n-1)
            if n-2 not in hashmap: hashmap[n-2] = fb(n-2)

            return hashmap[n-1] + hashmap[n-2]
        
        return fb(n)

        



            

