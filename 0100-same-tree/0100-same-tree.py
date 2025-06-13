# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None:
            if q != None:
                return False
            else :
                return True
        elif q == None:
            return False
        elif p.val != q.val:
            return False
        else:
            if self.isSameTree(p.left,q.left) == False:
                return False
            if self.isSameTree(p.right,q.right) == False:
                return False
            else:
                return True

        