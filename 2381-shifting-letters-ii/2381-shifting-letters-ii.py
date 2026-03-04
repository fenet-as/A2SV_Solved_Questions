class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0]*len(s)

        for l,r,d in shifts:
            d = -1 if d == 0 else 1

            prefix[l] += d
            if r+1 < len(s):
                prefix[r+1] -= d

        for i in range(1,len(s)):
            prefix[i] += prefix[i-1]

        chars = []
        for i in range(len(s)):
            shifted = ((ord(s[i]) - 97 )+ prefix[i])%26 + 97
            chars.append(chr(shifted))

        return ''.join(chars)
        
