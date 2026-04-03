# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        ind = {}
        for i,v in enumerate(nums):
            ind[v] = i

        
        def build(arr,i,j):
            if j-i+1 <= 0:
                return None
            
            mx = max(arr[i:j+1])

            node = TreeNode(mx)

            mi = ind[mx]
            node.left = build(arr,i,mi-1)
            node.right = build(arr,mi+1,j)

            return node

        return build(nums,0,len(nums)-1)

        