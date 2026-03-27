class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        seen = []
        res = []

        def check(arr):
            nonlocal n
            for i in range(n):
                for j in range(i+1,n):
                    i1,i2 = arr[i]
                    j1,j2 = arr[j]
                    if abs(i1-j1) == abs(j2-i2):
                        return False
            return True



        def explore():
            
            if len(seen) == n:
                act = []
                for i in range(len(seen)):
                    act.append([i,seen[i]])

                if check(act):
                    res.append(act[:])
                # print("res",res)
                # print("seen",seen)
                return 

            
            for j in range(n):
                if j in seen:
                    continue
                seen.append(j)
                # print("seen",seen)
                explore()
                seen.pop()
                # print("seen",seen)

            return 
        explore()

        ans = []

        for e in res:
            c = [["."]*n for _ in range(n)]
            for i,j in e:
                c[i][j] = "Q"

            for i in range(len(c)):
                c[i] = ''.join(c[i])
            ans.append(c)

                

        return ans

