# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversalList(self, root: Optional[TreeNode], output: List[int]) -> List[int]:
        if root == None:
            return output
        output = self.postorderTraversalList(root.left, output)
        output = self.postorderTraversalList(root.right, output)
        output.append(root.val)
        return output
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        return self.postorderTraversalList(root, output)
        