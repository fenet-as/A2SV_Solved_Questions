class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        

        res = []
        path = []

        def helper(i):
            if len(path) == k:
                res.append(path[:])
                return

            for j in range(i,n+1):
                path.append(j)
                helper(j+1)
                path.pop()

            return 
        helper(1)
        return res