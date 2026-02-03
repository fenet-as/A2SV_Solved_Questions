class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        num = list(str(x))
        return num == num[::-1]
