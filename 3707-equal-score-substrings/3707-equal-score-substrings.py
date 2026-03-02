class Solution:
    def scoreBalance(self, s: str) -> bool:
        l = 1 
        r = len(s)-1
        left = ord(s[0]) - 96
        right = 0
        while l <= r:
            if right < left:
                right += ord(s[r]) - 96
                r-=1
            else:
                left += ord(s[l]) - 96
                l+=1
            
        #print(left, right)
        return right == left