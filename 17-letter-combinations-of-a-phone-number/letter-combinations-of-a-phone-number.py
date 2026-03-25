class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        hm = {
            "2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
        }

        letters = []
        res = []

        def helper(i):
            if len(letters) == len(digits):
                res.append(''.join(letters))
                return 
            if i >= len(digits):
                return

            for e in hm[digits[i]]:
                letters.append(e)
                helper(i+1)
                letters.pop()
            return 

        helper(0)
        return res

