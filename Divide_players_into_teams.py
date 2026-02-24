class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)

        teams = n // 2
        total_skill = sum(skill)

        if total_skill % teams != 0:
            return -1

        each_skill = total_skill // teams 
        skill.sort()
        i = 0
        j = n - 1

        
        res = 0

        while i < j:
            if skill[i] + skill[j] != each_skill:
                return -1
            res += (skill[i] * skill[j])
            i += 1
            j -= 1
        return res 
        
