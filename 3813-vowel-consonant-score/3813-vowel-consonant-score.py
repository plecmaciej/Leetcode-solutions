class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v = 0
        c = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for letter in s:
            if 'a' <= letter <= 'z':
                if letter in vowels:
                    v += 1
                else:
                    c+=1
        if c > 0:
            return v // c
        else:
            return 0