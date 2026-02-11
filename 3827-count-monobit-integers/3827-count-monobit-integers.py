class Solution:
    def countMonobit(self, n: int) -> int:
        return ((n+1).bit_length())
        #return math.floor(math.log2(n+1)) + 1
