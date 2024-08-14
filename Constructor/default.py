class sum : 
    def __init__(self) :
        self.a = 0
        self.b = 0
    def read(self,x,y) :
        self.a = x
        self.b = y
    def show(self) :
        print("a : ",self.a)
        print("b : ",self.b)
    def sum(self) :
        c = self.a + self.b
        print("SUm : ",c)

obj = sum()
obj.read(4,8)
obj.show()
obj.sum()