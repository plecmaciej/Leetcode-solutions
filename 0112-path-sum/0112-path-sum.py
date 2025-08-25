# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findPath(self, root: Optional[TreeNode], targetSum: int) -> bool:
        targetSum = targetSum - root.val
        if root.left == None and root.right == None:
            if targetSum == 0:
                return True
            else:
                return False
        if root.left != None:
            if self.hasPathSum(root.left, targetSum) == True:
                return True
        if root.right != None:
            if self.hasPathSum(root.right, targetSum) == True:
                return True
        return False
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        return self.findPath(root, targetSum)
        