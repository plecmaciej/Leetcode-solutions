# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes_counter(self, root: Optional[TreeNode], number: Optional[int]) -> int:
        if root == None:
            return number
        number = self.countNodes_counter(root.left, number)
        number = self.countNodes_counter(root.right, number)
        return number + 1
    def countNodes(self, root: Optional[TreeNode]) -> int:
        number = 0
        return self.countNodes_counter(root, number)
