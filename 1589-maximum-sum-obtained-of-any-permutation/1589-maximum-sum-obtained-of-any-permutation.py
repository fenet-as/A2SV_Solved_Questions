class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        '''
         [1,2,3,4,5]
          0 1 2 3 4

         [0,1,3,6,10,15]

         2-4
         ps = ps[j+1] - ps[i]
              15 - 3 
        '''
        
        ind = [0] * (len(nums)+1)

        # for es,ee in requests:
        #     for j in range(es,ee+1):
        #         ind[j] += 1
        for es,ee in requests:
            ind[es] += 1
            ind[ee+1] -= 1
        
        indx = []

        cs = 0
        for e in ind:
            cs += e
            indx.append(cs)


        

        

        indz = []
        for i,v in enumerate(indx):
            indz.append((i,v))
        indz.sort(reverse=True, key = lambda x: x[1])

        nums.sort(reverse=True)


        za = []
        for i in range(len(nums)):
            ie = indz[i]

            za.append((ie[0],nums[i]))


        nnums = [0]*len(nums)

        for e in za:
            ind = e[0]
            val = e[1]
            nnums[ind] = val
        
        



        ps = [0]

        cs = 0
        for e in nnums:
            cs += e
            ps.append(cs)
        
        sm = 0

        for si,li in requests:

            csm = ps[li+1] - ps[si]
            sm += csm

        return (sm% (10**9 + 7))

