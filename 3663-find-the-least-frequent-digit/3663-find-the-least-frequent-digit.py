class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        freq = [0] * 10

        while n > 0:
            digit = n % 10
            freq[digit] += 1
            n //= 10

        smallest = 50
        digit = None

        for i in range(0,10):
            frequency_digit = freq[i] 
            if (frequency_digit != 0) and (frequency_digit < smallest):
                smallest = frequency_digit
                digit = i

        return digit