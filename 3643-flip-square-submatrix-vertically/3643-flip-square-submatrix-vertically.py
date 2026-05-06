class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        end_row = x + k - 1
        end_col = y + k
        while x < end_row: 
            grid[end_row][y:end_col], grid[x][y:end_col] = grid[x][y:end_col], grid[end_row][y:end_col]
            x += 1
            end_row -= 1
        
        return grid
