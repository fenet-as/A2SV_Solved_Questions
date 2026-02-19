class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])

        sr = points[0][0]
        er = points[0][1]
        ct = 0
        n = len(points)

        print(points)

        if len(points) == 1:
            return 1
        j = 1 
        while j < n:
            # print(i,j,ct)
            while j < n and points[j][0] <= er:
                sr = max(points[j][0],sr)
                er = min(points[j][1],er)
                j += 1

            ct += 1
            if j < n:
                sr = points[j][0]
                er = points[j][1]


            #     print("run")
            # print(i,j,ct)
        return ct
