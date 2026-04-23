"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:


        nodes = {e.id : e for e in employees }
         
        def dfs(node):
            if not node.subordinates:
                return node.importance

            t = 0

            for nei in  node.subordinates:
                e = nodes[nei]
                t += dfs(e)
                

            return t + node.importance

        
        for e in employees:
            if e.id == id:
                return dfs(e)




