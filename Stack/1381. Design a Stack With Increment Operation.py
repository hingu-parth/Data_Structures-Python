class CustomStack:

    def __init__(self, maxSize: int):
        self.stack=[]
        self.maxSize=maxSize
        

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(x)
        elif len(self.stack)!= self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        else:
            s=self.stack[len(self.stack)-1]
            self.stack.pop()
            return s


        

    def increment(self, k: int, val: int) -> None:
        if len(self.stack)<=k:
            for j,i in enumerate(self.stack):
                i+=val
                self.stack[j]=i
        elif k<=len(self.stack):
            for j,i in enumerate(self.stack[:k]):
                i+=val
                self.stack[j]=i
                


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)