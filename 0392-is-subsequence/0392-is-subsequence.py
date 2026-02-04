class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        left = 0
        if len(s) == 0:
            return True
        for i in range(len(t)):
            #print(left, t[i])
            if s[left] == t[i]:
                left += 1
            if left == len(s):
                return True
        if left == len(s):
            return True
        else:
            return False
