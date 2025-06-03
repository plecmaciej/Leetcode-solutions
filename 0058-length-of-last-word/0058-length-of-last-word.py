class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1
        inWord = False
        counter = 0
        while end>=0:
            if s[end] == ' ':
                if inWord:
                    return counter
            else:
                if not inWord:
                    inWord = True
                counter = counter + 1
            end -=1
        return counter
            