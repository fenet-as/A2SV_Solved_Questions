class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []

        def helper(path,i):

            if i > n+1:
                return 

            if len(path) == k:
                res.append(path[:])
                return
  
            path.append(i)
            helper(path,i+1)
            path.pop()
            
            helper(path,i+1)

        helper([],1)
        return res