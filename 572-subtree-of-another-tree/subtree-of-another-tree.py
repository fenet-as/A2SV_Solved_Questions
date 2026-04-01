# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def check(node,sub):
            if not node and not sub:
                return True
            if not node or not sub:
                return False

            if node.val != sub.val:
                return False

            left = check(node.left, sub.left)
            right = check(node.right,sub.right)

            return left and right

        
        def explore(node,sub):

            if check(node,sub):
                return True
            if not node:
                return False

            left = explore(node.left, sub)

            if left:
                return True
            right = explore(node.right,sub)

            if right:
                return True

            return False

   
        
        return explore(root,subRoot)


            
        