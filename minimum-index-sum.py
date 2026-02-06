class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:


        set1 = {}
        common = []

        for i,v in enumerate(list1):
            set1[v] = i


        for i,v in enumerate(list2):
            if v in set1 :
                common.append((v,set1[v]+i))

        common.sort(key=lambda x:x[1])

        res = []
        i = 0
        fe = common[i]
        res.append(fe[0])
        while i+1 < len(common) :
            se = common[i+1]
            if fe[1] == se[1]:
                res.append(se[0])
                i += 1
            else:
                break

        return res

            
