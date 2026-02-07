class Solution:
    def intToRoman(self, num: int) -> str:
        symbol = {
        1:"I",
        5:"V",
        10: "X",
        50:"L",
        100:"C",
        500:"D",
        1000:"M"
        }

        m = 1
        res = []
        while num > 0:
            digit = (num % 10) 
            n = digit * m
            num //= 10

            if digit == 0:
                pass
            elif digit == 1 or digit == 5:
                res.append(symbol[n])

            elif digit == 4:
                res.append((symbol[m] + symbol[m*5]))

            elif digit == 9:
                res.append((symbol[m]+symbol[10*m]))
            else:
                if 1< digit < 5:
                    res.append((symbol[m]*digit)) 
                else:
                    if digit == 6:
                        res.append((symbol[5*m] + symbol[m]))
                    elif digit == 7:
                        res.append((symbol[5*m] + symbol[m]*2))
                    else:
                        res.append((symbol[5*m] + symbol[m]*3))
            m *= 10
        res.reverse()

        return ''.join(res)

            


