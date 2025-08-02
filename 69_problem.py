class Employee:
    salary = 1234567
    increment = 20

    @property
    def SalaryafterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @SalaryafterIncrement.setter
    def SalaryafterIncrement(self, salary):
        self.increment = ((salary/self.salary) -1)*100


e = Employee()
#print(e.SalaryafterIncrement)
e.increment = 1358023.7
print(e.increment)

