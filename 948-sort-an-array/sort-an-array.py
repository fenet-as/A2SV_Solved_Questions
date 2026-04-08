class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        def merge(a1,a2):
            i = j = 0
            res = []
            while i < len(a1) and j < len(a2):
                if a1[i] < a2[j]:
                    res.append(a1[i])
                    i += 1
                else:
                    res.append(a2[j])
                    j += 1
            res.extend(a1[i:])
            res.extend(a2[j:])
            return res

        def mergeSort(l,r,arr):
            if l == r:
                return [arr[l]]
            m = (l+r)//2
            left = mergeSort(l,m,arr)
            right = mergeSort(m+1,r,arr)
            return merge(left,right)

        return mergeSort(0,len(nums)-1,nums)
        


                
            