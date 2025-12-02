class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x > y:
            longer_bin = bin(x)[2:]
            shorter_bin = bin(y)[2:]
        else:
            shorter_bin = bin(x)[2:]
            longer_bin = bin(y)[2:]
        hamming_distance = 0
        diff = len(longer_bin) - len(shorter_bin)
        
        for i in range(len(shorter_bin) - 1, -1, -1):
            if shorter_bin[i] != longer_bin[i + diff]:
                #print(i,shorter_bin[i], longer_bin[i + diff])
                hamming_distance += 1

        diff -=1
        while diff >=0:
            if longer_bin[diff] == '1':
               # print(longer_bin[diff], diff)
                hamming_distance += 1
            diff-=1
        return hamming_distance


