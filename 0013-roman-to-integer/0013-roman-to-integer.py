class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        previous = 0
        value = 0
        for i in range(len(s)):
            if s[i] == 'I':
                value = 1
            elif s[i] == 'V':
                value = 5
            elif s[i] == 'X':
                value = 10
            elif s[i] == 'L':
                value = 50
            elif s[i] == 'C':
                value = 100
            elif s[i] == 'D':
                value = 500     
            elif s[i] == 'M':
                value = 1000

            if previous < value:
               value = value - 2*previous

            number = number + value
            previous = value 
        return number 
