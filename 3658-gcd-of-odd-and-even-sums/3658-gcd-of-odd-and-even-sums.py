class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even_sum = n *( n + 1 )
        odd_sum = n * n
        return even_sum - odd_sum
