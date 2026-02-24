class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if (len(needle) > len(haystack)) or (needle not in haystack):
            return -1

        else:
            n = len(haystack)
            m = len(needle)

            i = 0
        
            for i in range(n):
                curr = i
                j = 0
                while curr < n and j < m and  needle[j] == haystack[curr]:
                    j += 1
                    curr += 1
                if j >= m:
                    return curr - m
            
        
                