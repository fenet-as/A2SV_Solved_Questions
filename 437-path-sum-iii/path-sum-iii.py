# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        ct = 0

        def dfs(node,cs):
            nonlocal ct
            if not node:
                return 

            cs += node.val
            if cs == targetSum:
                ct += 1

            dfs(node.left,cs)
            dfs(node.right,cs)
            return 

        def explore(node,cs):
            if not node:
                return 

            dfs(node,cs)

            explore(node.left,cs)
            explore(node.right,cs)
        
        
        explore(root,0)
        return ct