class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        max_height = max(heights)

        count = [""] * (max_height + 1)
        # count = ["", "", "", ......, "John", "", ....."Emma", ...., "Mary"]
        #                              165              170       180
        for i in range(len(heights)):
            count[heights[i]] = names[i]

        result = []
        for j in range(len(count) - 1, -1, -1):
            if count[j] != "":
                result.append(count[j])

        return result
