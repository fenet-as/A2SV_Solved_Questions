class Solution:
    def splitString(self, s: str) -> bool:
        
        path = []
        def choose(s,i):
            # print(path)
            if i == len(s) and len(path) >= 2:
                return True

            for j in range(i,len(s)):
                curr = int(s[i:j+1])
                if path and path[-1] - curr != 1:
                    continue
                path.append(curr)
                if choose(s,j+1):
                    return True
                
                path.pop()
                #print(path)
            return False

        return choose(s,0)


