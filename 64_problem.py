class Calculator:
    def __init__(self , n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")

    @staticmethod
    def Hello():
        print("Hello World ")

a = Calculator(4)
a.Hello()
a.square()
a.cube()
a.squareroot()
