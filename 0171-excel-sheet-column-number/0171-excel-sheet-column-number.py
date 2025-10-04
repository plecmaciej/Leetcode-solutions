class Solution:

    def changeAZToInt(self, letter: str) -> int:
        return ord(letter) - 64
    def titleToNumber(self, columnTitle: str) -> int:
        output = 0
        power = 1
        for i in range(len(columnTitle) - 1, -1, -1):
            output += self.changeAZToInt(columnTitle[i]) * power
            power = power * 26
        return output