class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()
        # print(position)
        i = 1
        j = max(position) - min(position)
        ans = -1

        def possible(mid, k,arr):
            sp = arr[0]

            ct = 1

            for e in arr:
                
                d = e - sp
                # print(e,d)
                if d >= mid:
                    ct += 1
                    sp = e

                if ct == k:
                    # print("ct",ct)
                    return True

            return False

                





        while i <= j:

            mid = i + (j-i)//2
            # print(mid)

            if possible(mid,m,position):
                ans = mid
                i = mid+1
                # print("ans", ans)
            else:
                j = mid-1
        return ans  