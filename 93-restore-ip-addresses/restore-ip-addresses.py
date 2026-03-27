class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []

        res = []
        path = []
        def explore(i,s):
            if len(path) == 4 and i == len(s):
                res.append('.'.join(path))
                return 
            elif len(path) == 4 and i < len(s):
                return 

           
            for j in range(i,len(s)):
                if (len(s)-j) / (4-len(path)) <= 0 or (len(s)-j) / (4-len(path)) > 3:
                    continue

                curr = s[i:j+1]
                if len(curr) > 3:
                    break
                if len(curr) > 1 and s[i] == "0":
                    break
                if int(curr) > 255:
                    break
               
                path.append(curr)
                explore(j+1,s)
                path.pop()

            return 

        explore(0,s)
        return res

                


