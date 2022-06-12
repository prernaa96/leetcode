# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# nums=[]
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root == None:
            return None
        
        def inorder(root):
        
            if root:
                inorder(root.left)
                nums.append(root.val)
                inorder(root.right)      
            return nums
        
        nums=[]
        ans = inorder(root)
        return ans
        