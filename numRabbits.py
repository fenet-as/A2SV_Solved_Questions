class Solution:
    def numRabbits(self, answers: List[int]) -> int:


        hm = {}

        ct = 0

        for e in answers:
            if e == 0:
                ct += 1
            elif e not in hm:
                hm[e] = [1,e+1]
                ct += (e+1)
                

            elif (hm[e][0] + 1) > hm[e][1]:
                hm[e][1] *= 2
                hm[e][0] += 1
                ct += (e + 1)
         
            else:
                hm[e][0] += 1
             
            # print(hm,ct)
        return ct

