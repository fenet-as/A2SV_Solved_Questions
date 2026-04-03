class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        path = []
        
        candidates.sort()
    

        def explore(i,rem):
            if rem == 0:
                res.append(path[:])
                return


            for j in range(i,len(candidates)):

                if j > i and candidates[j-1] == candidates[j]:
                    continue

                if candidates[j] > rem:
                    break

                path.append(candidates[j])                
                explore(j+1,rem - candidates[j])
                path.pop()

            return 
        explore(0,target)

        return res






                

        