"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
        #
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:


        nodes = {e.id : e for e in employees }
         
        def dfs(node):
            t = node.importance

            for nei in  node.subordinates:
                e = nodes[nei]
                t += dfs(e)
                

            return t

    
        return dfs(nodes[id])




