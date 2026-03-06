class Solution:
    def countSegments(self, s: str) -> int:
        if len(s) == 0 :
            return 0
        counter = 0
        inWord = False
        for i in range(len(s)):
            if s[i] == ' ' :
                if inWord:
                    counter += 1
                    inWord = False
            else:
                inWord = True
        if s[-1] != ' ':
            counter += 1
        return counter