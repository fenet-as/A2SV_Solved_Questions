class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        ps = [0]*len(nums)

        n = len(nums)
        for l,r in requests:
            ps[l] += 1
            if r+1 < n:
                ps[r+1] -= 1

        for i in range(1,n):
            ps[i] += ps[i-1]


        for i in range(n):
            v = ps[i]
            ps[i] = (i,v)

        ps.sort(key = lambda x:x[1])
        nums.sort()
        # print(ps)
        # print(nums)


        

        rs = [0]*n

        for i in range(n):
            ind = ps[i][0]
            v = nums[i]
            rs[ind] = v

        # print(rs)


        for i in range(1,n):
            rs[i] += rs[i-1]

        sm = 0

        for l,r in requests:
            e = rs[r]
            s = 0 if l == 0 else rs[l-1]
            sm += e - s
        return sm%(10**9+7)
