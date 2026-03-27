class Solution:
    def isAdditiveNumber(self, nums: str) -> bool:
        
        path = []

        

        def explore(i):
            if i == len(nums):
                if len(path) >= 3:
                    return True

            
            for j in range(i,len(nums)):
                curr = int(nums[i:j+1])
                # print("curr " ,curr)
                if j-i+1 > 1 and nums[i] == "0":
                    continue

                
                
                if len(path) < 2 or  (len(path) >= 2 and  path[-1] + path[-2] == curr):
                    path.append(curr)
                    # print("path ",path)
                    if explore(j+1):
                        return True
                    path.pop()
                    # print("path ",path)
                elif path[-1] + path[-2]  < curr:
                    break

                
                
                    
            return False

        return explore(0)
                
