# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        first = None
        last = None
        middle = None
        prev = None

        def dfs(node):
            nonlocal prev,middle,last,first
            if not node: return 

            dfs(node.left)

            if prev and prev.val > node.val:

                if not first: 
                    first = prev
                    middle = node

                else:
                    last = node 
            
            prev = node 

            dfs(node.right)

        
        dfs(root)

        if last:
            first.val,last.val = last.val, first.val

        else:
            first.val,middle.val = middle.val,first.val

        return root

        