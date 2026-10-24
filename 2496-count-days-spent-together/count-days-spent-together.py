class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        

        def find_days_ct(d):

            months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            m = int(d[:2])
            dy = int(d[3:])
            sm = 0
            for i in range(m-1):
                sm += months[i]

            sm += dy

            return sm
        

            


        aa = find_days_ct(arriveAlice)
        la = find_days_ct(leaveAlice)
        ab = find_days_ct(arriveBob)
        lb = find_days_ct(leaveBob)

        if la < ab or lb < aa: return 0

        return min(la,lb) - max(aa,ab) + 1