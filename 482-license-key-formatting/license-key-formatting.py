class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        word = list(''.join(s.split("-")))

        chars = []

        for e in word:
            if e.isalpha():
                chars.append(e.upper())

            else:
                chars.append(e)

        dashes = len(chars)//k

        ans = []

        i = len(chars) - k
        j = len(chars)

        while i >= 0:
            ans.append(''.join(chars[i:j]))
            j -= k
            i -= k
        if len(chars)%k != 0:
            ans.append(''.join(chars[:j]))

        ans.reverse()

        return ('-'.join(ans))


        