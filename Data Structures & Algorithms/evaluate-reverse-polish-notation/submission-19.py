class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in range(len(tokens)):
            t = tokens[i]
            if t == "+":
                n1 = stk.pop()
                n2 = stk.pop()
                stk.append(n1 + n2)
            elif t == "-":
                n1 = stk.pop()
                n2 = stk.pop()
                stk.append( n2 - n1)
            elif t == "*":
                n1 = stk.pop()
                n2 = stk.pop()
                stk.append( n2*n1)
            elif t == "/":
                n1 = stk.pop()
                n2 = stk.pop()
                stk.append( int(n2/n1))
            else:
                stk.append(int(t))
        return stk.pop()

        