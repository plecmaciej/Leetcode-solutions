class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n = format(n,f'0{32}b')
        reversed_bin_n = bin_n[::-1]
        sum_to_int = int(reversed_bin_n,2)
        print(sum_to_int)
        return sum_to_int
