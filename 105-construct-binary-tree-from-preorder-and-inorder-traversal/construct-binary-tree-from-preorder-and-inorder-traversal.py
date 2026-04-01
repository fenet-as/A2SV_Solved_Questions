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
        def build(l,r):
            nonlocal i
            if l > r:
                return None

            node = TreeNode(preorder[i])

            pt = find_ind[preorder[i]]
            i += 1
  
            node.left = build(l,pt-1)
            node.right = build(pt+1,r)

            return node

        return build(0,len(inorder)-1)

