class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Fill sets with existing numbers
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = board[i][j]
                    box = (i // 3) * 3 + (j // 3)

                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box].add(num)

        def solve():

            for i in range(9):
                for j in range(9):

                    if board[i][j] == ".":

                        box = (i // 3) * 3 + (j // 3)

                        for n in "123456789":

                            if n not in rows[i] and \
                               n not in cols[j] and \
                               n not in boxes[box]:

                                board[i][j] = n
                                rows[i].add(n)
                                cols[j].add(n)
                                boxes[box].add(n)

                                if solve():
                                    return True

                                # Backtrack
                                board[i][j] = "."
                                rows[i].remove(n)
                                cols[j].remove(n)
                                boxes[box].remove(n)

                        return False

            return True

        solve()