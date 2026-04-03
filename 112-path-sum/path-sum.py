# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        

        def explore(node,cs):
            if not node:
                return False
            if not node.left and not node.right:
                if cs + node.val == targetSum:
                    return True
                return False


            left = explore(node.left,cs + node.val)
            right = explore(node.right,cs + node.val)
            return left or right 

       

        return explore(root,0)

