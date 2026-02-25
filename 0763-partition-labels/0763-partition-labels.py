class Solution:
    def partitionLabels(self, s: str) -> List[int]:



        hm = {}


        for i in range(len(s)-1,-1,-1):
            if s[i] not in hm:
                hm[s[i]] = i

    
        i = 0

        res = []
        while i < len(s):
            start = i
            end = hm[s[i]]

            while i <= end:
                if hm[s[i]] > end:
                    end = hm[s[i]]
                i += 1
                

            res.append(i - start)
        return res
    