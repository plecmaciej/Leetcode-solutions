class Solution:

    def changeToAZ(self, number: int) -> str:
        if number == 0:
            return chr(90) 
        else:
            return chr(number + 64)

    def convertToTitle(self, columnNumber: int) -> str:
        output = ""
        while columnNumber != 0:
            number = columnNumber % 26
            output+=self.changeToAZ(number)
            columnNumber = columnNumber // 26
            if number == 0:
                columnNumber -=1
        return output[::-1]