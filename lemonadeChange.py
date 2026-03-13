class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        hm = defaultdict(int)

        for e in bills:
            if e == 20:
                if hm[10] > 0 and hm[5] > 0:
                    hm[10] -= 1
                    hm[5] -= 1
                elif hm[5] >= 3:
                    hm[5] -= 3
                else:
                    return False

            elif e == 10:
                if hm[5] > 0:
                    hm[5] -= 1
                else:
                    return False
            hm[e] += 1
            # print(hm)
        return True
