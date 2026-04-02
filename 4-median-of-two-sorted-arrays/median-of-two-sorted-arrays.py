class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

        merged = []

        i = 0
        j = 0

        n = (len(nums1) + len(nums2))


        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])


        

        if n % 2 == 0:
            fi = (n//2)-1
            li = n//2
            return (merged[fi] + merged[li])/2
        else:
            return merged[n//2]

        
    

