class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        2:39pm 2:44pm
        only 1 mistake on line 12 used "box" when I should have used board. Typo
        """
        rowsets = [set() for _ in range(9)]
        colsets = [set() for _ in range(9)]
        boxsets = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                s = board[r][c]
                if s == ".":
                    continue
                rset = rowsets[r]
                cset = colsets[c]
                box_id = (r//3) * 3 + c//3
                bset = boxsets[box_id]
                if s in rset:
                    return False
                else:
                    rset.add(s)
                if s in cset:
                    return False
                else:
                    cset.add(s)
                if s in bset:
                    return False
                else:
                    bset.add(s)
        return True


