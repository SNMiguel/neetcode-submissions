class MinStack:

    def __init__(self):
        self.elements = []

    def push(self, val: int) -> None:
        if not self.elements:
            cur_min = val
        else:
            cur_min = min(val, self.elements[-1][1])
        self.elements.append((val, cur_min))

    def pop(self) -> None:
        self.elements.pop()

    def top(self) -> int:
        return self.elements[-1][0]

    def getMin(self) -> int:
        return self.elements[-1][-1]
        
