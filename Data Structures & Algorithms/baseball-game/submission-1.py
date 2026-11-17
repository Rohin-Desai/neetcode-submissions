class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for s in operations:
            if s == "+":
                n1 = stk[-1]
                n2 = stk[-2]    
                stk.append(n1 + n2)
            elif s == "D":
                n1 = stk[-1]
                stk.append(2*n1)
            elif s == "C":
                stk.pop()
            else: #is a number
                n = int(s)
                stk.append(n)
        return sum(stk)