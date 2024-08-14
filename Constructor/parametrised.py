class add :
    def __init__(self,a,b) :
        self.x = a
        self.y = b
        self.z = a+b
    def show(self) :
        print("sum : ",self.z)
obj = add(9,369)
obj.show()