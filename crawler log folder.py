class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        count = 0

        for c in logs:
            if c == "../" :
                if count > 0:count -= 1
            elif c == "./" : count 
            else: count += 1
          
        return count 
