# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        find_ind = {}
        for i,v in enumerate(inorder):
            find_ind[v] = i



        i = 0
        def build(left,right):
            nonlocal i
            if left > right:
                return None

            ind = find_ind[preorder[i]]
            node = TreeNode(preorder[i])

            i += 1

            node.left = build(left,ind-1)
            node.right = build(ind+1,right)

            return node

        return build(0,len(preorder)-1) 