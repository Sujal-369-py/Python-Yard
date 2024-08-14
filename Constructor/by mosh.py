class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("Self")


point1 = Point(3,6)
print(point1.x,point1.y)
       