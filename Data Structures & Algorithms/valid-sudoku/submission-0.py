class Solution:
    def tbt(self, grid: List[int]) -> bool:
        return len([x for x in grid if x != 0]) == len(set(x for x in grid if x != 0))
    def col(self, column: List[int]) -> bool:
        return len([x for x in column if x != 0]) == len(set(x for x in column if x != 0))
    def row(self, line: List[int]) -> bool:
        return len([x for x in line if x != 0]) == len(set(x for x in line if x != 0))
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            i = [int(x) if x.isdigit() else 0 for x in i]
            if not self.row(i):
                return False
        for j in range(9):
            column = [0 if line[j] == "." else int(line[j]) for line in board]
            if not self.col(column):
                return False
        for r0 in range(0, 9, 3):
            for c0 in range(0, 9, 3):
                block = [
                    0 if board[r][c] == "." else int(board[r][c])
                    for r in range(r0, r0+3)
                    for c in range(c0, c0+3)
                ]
                if not self.tbt(block):
                    return False
        return True

