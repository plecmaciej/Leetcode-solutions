# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_left_list(self, root: Optional[TreeNode], ver_list: Optional[list]) -> list:
        if root == None:
            ver_list.append(-1)
            return ver_list
        ver_list.append(root.val)
        ver_list = self.get_left_list(root.left, ver_list)
        ver_list = self.get_left_list(root.right, ver_list)
        return ver_list

    def get_right_list(self, root: Optional[TreeNode], ver_list: Optional[list]) -> list:
        if root == None:
            ver_list.append(-1)
            return ver_list
        ver_list.append(root.val)
        ver_list = self.get_right_list(root.right, ver_list)
        ver_list = self.get_right_list(root.left, ver_list)
        return ver_list

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        left_list = []
        right_list = []
        left_list = self.get_left_list(root.left, left_list)
        right_list = self.get_right_list(root.right, right_list)
        length = len(left_list)
        if length != len(right_list):
            return False
        for i in range(length):
            if right_list[i] != left_list[i]:
                return False
        return True