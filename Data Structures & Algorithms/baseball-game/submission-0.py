class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for o in range(len(operations)):
            if operations[o] == '+':
                stack.append(stack[-1] + stack[-2])
            elif operations[o] == 'D':
                stack.append(stack[-1]*2)
            elif operations[o] == 'C':
                stack.pop()
            else:
                stack.append(int(operations[o]))
        sum = 0
        for ele in stack:
            sum += ele
        return sum

            

        

    
            
