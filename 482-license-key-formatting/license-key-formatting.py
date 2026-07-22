class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans = []
        count = 0

        res = []
        for c in s[::-1]:
            if c != "-":
                count += 1
                res.append(c.upper())
            if count == k:
                count = 0
                ans.append(''.join(res))
                ans.append("-")
                res = []
        ans.append(''.join(res))
     
        ans = ''.join(ans)
        

        if len(ans) != 0 and ans[-1] == "-":
            ans = ans[:-1]
        ans = ans[::-1]
        
        return ans 


