class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        

        res = []

        sm = 0
        for _ in range(num):

            nsm = sm + 9

            if nsm > sum:
                c = 9 - (nsm - sum) 
                sm += c
                res.append(str(c))

            else:
                
                sm += 9
                res.append("9")


        if sm != sum: return ""
        return ''.join(res)
            