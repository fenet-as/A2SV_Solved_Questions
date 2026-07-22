class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []

        path = []


        def move(j):
            if len(path) == k:
                res.append(path.copy())
                return True

            for i in range(j+1,n+1):
                path.append(i)
                if move(i):
                    path.pop()
            
            return True
        move(0)
        return res

