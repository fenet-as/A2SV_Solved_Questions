# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        seen = set()

        def dfs(node,k):
            if not node:
                return 

            if k - node.val in seen:
                return True
            seen.add(node.val)

            left = dfs(node.left,k)
            right = dfs(node.right,k)
            return left or right

        res = dfs(root,k)

        if res:
            return True
        return False

        