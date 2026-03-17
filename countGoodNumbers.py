class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        even_pos = 0
        odd_pos = 0

        if n % 2 == 0:
            even_pos = odd_pos = n // 2
        else:
            even_pos = (n+1)//2
            odd_pos = even_pos -1

        
        mod = 10**9 + 7
        return (pow(5, even_pos, mod) * pow(4, odd_pos, mod)) % mod
