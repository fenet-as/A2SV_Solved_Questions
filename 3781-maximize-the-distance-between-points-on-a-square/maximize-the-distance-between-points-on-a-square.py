from bisect import bisect_left
class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        
        pos = []
        for x, y in points:
            if y == 0:
                pos.append(x)
            elif x == side:
                pos.append(side + y)
            elif y == side:
                pos.append(2 * side + (side - x))
            else:
                pos.append(3 * side + (side - y))
        
        pos.sort()
        n = len(pos)
        perimeter = 4 * side

        extended = pos + [p + perimeter for p in pos]




        def possible(x):
            for start in range(n):
                count = 1
                curr = extended[start]
                idx = start

                while count < k:
                    nxt = bisect_left(extended, curr + x, idx + 1)

                    if nxt >= start + n:
                        break

                    curr = extended[nxt]
                    idx = nxt
                    count += 1

                if count >= k:
                    
                    if curr - extended[start] <= perimeter - x:
                        return True

            return False


        i = 0
        j = 2 * side
        ans = 0

        while i <= j:
            mid = i + (j - i) // 2

            if possible(mid):
                ans = mid
                i = mid + 1   
            else:
                j = mid - 1   

        return ans