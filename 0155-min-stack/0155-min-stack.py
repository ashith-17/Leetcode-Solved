class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = None

    def push(self, val):
        if not self.stack:
            self.stack.append(val)
            self.minVal = val

        elif val >= self.minVal:
            self.stack.append(val)

        else:
            encoded = 2 * val - self.minVal
            self.stack.append(encoded)
            self.minVal = val

    def pop(self):
        top = self.stack.pop()

        if top < self.minVal:
            self.minVal = 2 * self.minVal - top

        if not self.stack:
            self.minVal = None

    def top(self):
        top = self.stack[-1]

        if top < self.minVal:
            return self.minVal

        return top

    def getMin(self):
        return self.minVal