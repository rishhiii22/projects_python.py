class TwoDVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"The vector is {self.i}i and {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
    def show(self):
        print(f"The vector is {self.i}i and {self.j}j and {self.k}k")

a = TwoDVector(1 ,2)
a.show()
b = ThreeDVector(4, 2, 6)
b.show()
        