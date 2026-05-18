# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0


        def dfs(node):
            nonlocal max_sum
            if not node:
                return True,float('-inf'), 0,float('inf')

            l_bst,l_max,lts,l_min = dfs(node.left)
            r_bst,r_max,rts,r_min = dfs(node.right)

            if l_bst and r_bst and l_max < node.val < r_min:
                ts = lts + rts + node.val

                max_sum = max(max_sum,ts)

                mn = min(l_min,node.val)
                mx = max(r_max,node.val)

                return True,mx,ts,mn

            return False,0,0,0

        c_bst,c_max,cts,c_min = dfs(root)
        return max_sum

            