# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        hm = set()

        def dfs(node,k):
            if not node:
                return 

            if k - node.val in hm:
                return True
            hm.add(node.val)

            l = dfs(node.left,k)
            r = dfs(node.right,k)
            return l or r

        res = dfs(root,k)

        if res:
            return True
        return False

        