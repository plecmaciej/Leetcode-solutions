class Solution:
    def findComplement(self, num: int) -> int:
        complement = 0
        power = 0
        while num > 0:
            if num%2 == 0:
                complement += pow(2,power)
            num = num//2
            power +=1
        return complement

