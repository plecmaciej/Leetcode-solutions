class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        if rowIndex == 0:
            return row
        for i in range(rowIndex):
            new_row = [1]
            for i in range(len(row)-1): 
                new_row.append(row[i] + row[i+1])
            new_row.append(1)
            row = new_row
        return new_row