class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        ans = ''
        count = 0

        for c in s[::-1]:
            if c != "-":
                count += 1
                ans += c.upper()
            if count == k:
                count = 0
                ans += "-"

        if len(ans) != 0 and ans[-1] == "-":
            ans = ans[:-1]
        ans = ans[::-1]
        
        return ans 


