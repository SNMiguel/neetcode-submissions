class Solution:
    def Checkrow(self, board: List[List[str]], i: int):
        row = []
        for j in range(9):
            if board[i][j] != ".":
                row.append(int(board[i][j]))
        return len(row) == len(set(row))

    def Checkcolumn(self, board: List[List[str]], i: int):
        column = []
        for j in range(9):
            if board[j][i] != ".":
                column.append(int(board[j][i]))
        return len(column) == len(set(column))

    def Checkbox(self, board: List[List[str]]):
        boxes_i = [(0, 0), (3, 0), (6, 0), (0, 3), (3, 3), (6, 3), (0, 6), (3, 6), (6, 6)]
        box = []
        for x, y in boxes_i:
            box.append(board[x][y])
            box.append(board[x][y + 1])
            box.append(board[x][y + 2])
            box.append(board[x + 1][y])
            box.append(board[x + 1][y + 1])
            box.append(board[x + 1][y + 2])
            box.append(board[x + 2][y])
            box.append(board[x + 2][y + 1])
            box.append(board[x + 2][y + 2])
            r_box = [int(x) for x in box if x != "."]
            if len(r_box) != len(set(r_box)):
                return False
                break
            box = []

        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not (self.Checkrow(board, i) & self.Checkcolumn(board, i)):
                return False
                break
        #self.Checkbox(board)
        return True & self.Checkbox(board)




        