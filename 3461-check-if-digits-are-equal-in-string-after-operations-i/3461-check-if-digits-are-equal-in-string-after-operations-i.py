class Solution:
    def hasSameDigits(self, s: str) -> bool:
        arr = [int(c) for c in s]
        length = len(arr)
        while length > 2:
            #print(arr)
            for i in range(length-1):
                arr[i] = (arr[i] + arr[i+1]) % 10
            length -= 1

        return arr[0] == arr[1]