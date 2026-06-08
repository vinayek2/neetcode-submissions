from collections import defaultdict
class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''

        create a hashset for every single column 
        create a hashset for every single row
        
        hashset for every 3x3 grid

        key (r/3, c/3) box coordinates 

        val -> hash set
        

        '''
        cols = defaultdict(set)
        
        rows = defaultdict(set)

        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if(board[r][c] == "."):
                    continue
                if(board[r][c] in rows[r] or
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r//3, c//3)] ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True
                    
        
        
        

        
        
        


