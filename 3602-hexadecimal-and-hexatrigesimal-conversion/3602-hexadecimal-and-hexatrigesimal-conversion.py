from collections import deque

class Solution:
    def concatHex36(self, n: int) -> str:
        val_n_2 = n * n
        val_n_3 = val_n_2 * n 
        hex(val_n_2)

        DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = deque()
        print(val_n_3)

        while val_n_3 > 0:
            val_n_3, rem = divmod(val_n_3, 36)
            result.appendleft(DIGITS[rem])

        return (format(val_n_2, 'X')) + ''.join(result)

