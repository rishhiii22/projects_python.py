class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pincode):
        self.name =name
        self.salary =salary
        self.pincode =pincode
        
p = Programmer("Rishi" , 12000000 , 324009)
print(p.name , p.salary , p.company, p.pincode)

r = Programmer("Virat" , 12000000 , 324009)
print(r.name , r.salary , r.company, r.pincode)