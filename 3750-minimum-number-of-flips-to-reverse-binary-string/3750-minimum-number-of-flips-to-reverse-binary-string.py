class Solution:
    def minimumFlips(self, n: int) -> int:
        binary = bin(n)[2:] 
        left = 0 
        right = len(binary) - 1
        reverse_counter = 0
        while left < right:
            if binary[left] != binary[right]:
                reverse_counter += 2
            left += 1
            right += -1
        return reverse_counter