class Solution:
    def countAndSay(self, n: int) -> str:
        

        def rle(s):
            i = 0
            j = 0

            res = []


            while j < len(s):
                
                while j < len(s) and s[i] == s[j]:
                    j += 1

                

                ct = j-i
                res.append(str(ct))
                res.append(s[i])

                i = j

            return ''.join(res)




        if n == 1 : return "1"

        s = 1
        p = "1"
        
        while s < n:
            p = rle(p)
            s += 1
            

        return p

