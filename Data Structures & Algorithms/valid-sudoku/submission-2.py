class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]

                if val == ".":
                    continue
                
                grid_idx = (row // 3) * 3 + (col // 3)

                if val in rows[row]:
                    return False
                
                if val in cols[col]:
                    return False

                if val in grid[grid_idx]:
                    return False

                rows[row].add(val)
                cols[col].add(val)
                grid[grid_idx].add(val)

        return True
        