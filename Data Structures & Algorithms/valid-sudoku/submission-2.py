class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        First attempt. Indexing a 2-D array. 
        I am sure there are more optimal readable ways.
        oops. Didn't read carefull. Board can be empty, but 
        constraints must be obeyed:
        digits can be from 1 to 9 and no duplicates.
        """
        nineset = set(["1","2","3","4","5","6","7","8","9"])
        b = board
        for i in range(9): #ROW
            row = b[i]
            s = set()
            for r in row:
                if r in s:
                    return False #DUP
                elif r == ".":
                    continue
                else:
                    s.add(r)
            for z in s:
                if z not in nineset:
                    return False
        for k in range(9):#over k cols
            s = set()
            for j in range(9):
                c = b[j][k]
                if c in s: 
                    return False
                elif c == ".":
                    continue
                else:
                    s.add(c)
            for z in s:
                if z not in nineset:
                    return False
            
        #Now each of the 3 blocks
        #i,j  (0,2) (0,2)
        #     (0,2) (3,5)
        #     (0,2) (6,8)
        #     (3,5) (0.2)
        #.    (3,5) (3,5)
        #     (3,5) (6,8)
        #     (6,8) (0.2)
        #     (6,8) (3,5)
        #     (6,8) (6,8)
        for i in [0,3,6]:
            for j in [0,3,6]:
                #ONE BLOCK
                s = set()
                for u in range(i, i+3):
                    for v in range(j, j+3):
                        c = b[u][v]
                        if c in s:
                            return False
                        elif c == ".":
                             continue
                        else:
                            s.add(c)
                for z in s:
                    if z not in nineset:
                        return False
        return True

                

        