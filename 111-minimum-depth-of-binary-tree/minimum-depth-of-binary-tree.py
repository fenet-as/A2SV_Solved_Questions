# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:


        def dfs(node):
            if not node:
                return 0


            l = dfs(node.left)
    
            r = dfs(node.right)

            if not node.left and not node.right:
                return 1
            elif not node.left:
                return 1 + r
            elif not node.right:
                return 1 + l
            else:
                return 1 + min(r,l)
       

        return dfs(root)
