class Demo:
    a = 4

p = Demo()
print(p.a) # Prints the class attribute because Instance Attribute is not present

p.a = 0 # Instance attribute is set

print(p.a) # Prints the Instance Attribute because instance attribute is present

print(Demo.a) # Prints the Class Attribute