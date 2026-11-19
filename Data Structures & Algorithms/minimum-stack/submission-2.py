class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        if len(self.stk) == 0:
            self.stk.append((val,val))
        else:
            _,previousMin = self.stk[-1]
            if previousMin < val:
                self.stk.append((val, previousMin))
            else:
                self.stk.append((val,val))
        

    def pop(self) -> None:
        self.stk.pop()
        

    def top(self) -> int:
        v,_ = self.stk[-1]
        return v
        

    def getMin(self) -> int:
        _, theMin = self.stk[-1]
        return theMin
        
