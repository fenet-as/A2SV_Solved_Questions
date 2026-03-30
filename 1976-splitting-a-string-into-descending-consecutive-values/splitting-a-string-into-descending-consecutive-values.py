class Solution:
    def splitString(self, s: str) -> bool:

        path = []
        def split(i):
            if i == len(s) and len(path) >= 2:
                return True

            for j in range(i,len(s)):
                w = s[i:j+1]

            
                if path and path[-1] - int(w) != 1:
                    continue
                
                path.append(int(w))
                # print(path)
                if split(j+1):
                    return True
                path.pop()
                # print(path)
            return False

        return split(0)




                
                
