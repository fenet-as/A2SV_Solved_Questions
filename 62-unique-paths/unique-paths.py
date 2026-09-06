class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        hm = {}

        def move(cr,cc):
            if cr == m-1 and cc == n-1:return 1

            if (cr,cc) in hm : return hm[(cr,cc)]

            ls = 0
            rs = 0

            if cr != m-1:ls = move(cr+1,cc)

            if cc != n-1: rs = move(cr,cc+1)


            res = ls + rs
            hm[(cr,cc)] = res

            return res

        return move(0,0)

        