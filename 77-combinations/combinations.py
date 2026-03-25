class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []

        def helper(path,i,k):
            if len(path) == k:
                res.append(path[:])
                return

            
            for j in range(i,n+1):
                path.append(j)
                helper(path,j+1,k)
                path.pop()

            return

        helper([],1,k)
        return res