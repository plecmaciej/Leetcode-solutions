class Solution:
    def balancedStringSplit(self, s: str) -> int:
        splits = 0
        r = 0
        l = 0
        for letter in s:
            if letter == 'R':
                r+=1
            else:
                l+=1
            if r==l : 
                splits+=1
                r=0
                l=0
        return splits
