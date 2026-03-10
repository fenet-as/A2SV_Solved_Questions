class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        st = []

        hm = {}

        for e in reversed(nums2):
            while st and st[-1] < e:
                st.pop()
            if st:
                hm[e] = st[-1]
            else:
                hm[e] = -1
                
            st.append(e)

        res = []
        for e in nums1:
            res.append(hm[e])
        return res
