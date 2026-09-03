class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')
        min_even = float('inf')


        for e in nums1:
            if e % 2 == 0:
                min_even = min(min_even,e)
            else:
                min_odd = min(min_odd,e)
        
        if min_odd == float('inf') or min_even == float('inf'):
            return True


        even_possible = True
        
        #try to make all even
        for e in nums1:
            if e % 2 != 0 and  e - min_odd < 1:
                even_possible = False
                break

        odd_possible = True
        
        #try all odd
        for e in nums1:
            if e % 2 == 0 and e - min_odd < 1:
                odd_possible = False
                break

        if odd_possible or even_possible: return True
        return False

