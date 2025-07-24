# Code for converting inches into cm.

def inch_to_cm(inch):
    return inch*2.54
n = int(input("Enter value in inches: "))
c = inch_to_cm

print(f"The corresponding value in cms is {c(n)}")