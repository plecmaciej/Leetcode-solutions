class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        row = [1]
        triangle = [row]
        while numRows > 1:
            new_row = [1]
            for i in range(len(triangle[-1])-1):
                new_row.append(triangle[-1][i] + triangle[-1][i+1])
            new_row.append(1)
            triangle.append(new_row)
            numRows -= 1
        return triangle
