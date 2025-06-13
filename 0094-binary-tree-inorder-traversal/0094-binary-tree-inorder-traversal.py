# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trav(self, root: Optional[TreeNode], new_list: List[int]) -> List[int]:
        if root.left !=None:
            new_list = self.trav(root.left, new_list)
        new_list.append(root.val)
        if root.right!= None:
            new_list = self.trav(root.right,new_list)
        return new_list
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        new_list = []
        if root == None:
            return new_list
        new_list = self.trav(root, new_list)
        return new_list
        