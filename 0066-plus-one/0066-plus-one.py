class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        end = len(digits)-1
        while end > 0:
            if digits[end] != 9:
                digits[end] += 1
                return digits
            else:
                digits[end] = 0
            end -= 1
        if digits[end] == 9:
            digits[end] = 0
            digits.insert(0,1)
        else:
            digits[end] +=1
        return digits

        
