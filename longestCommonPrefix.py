class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs[0])
        print(strs[0])

        res = ""
        fw = strs[0]
        for i in range(n):
            for w in strs:
                lw = len(w)
                
                if i > lw - 1:
                    return res
                if fw[i] != w[i]:
                    return res

            else:
                res += w[i]
        return res
