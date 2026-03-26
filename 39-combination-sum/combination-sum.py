class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        path = []

        

    #  candidates.sort()

        def choose(i,total):
            if total == target :
                res.append(path[:])
                return


            
            for j in range(i,len(candidates)):
                if total + candidates[j] <= target:
                    path.append(candidates[j])
                    choose(j,total+candidates[j])
                    path.pop()

            return 

        choose(0,0)
        return res

        


                

 
            

            