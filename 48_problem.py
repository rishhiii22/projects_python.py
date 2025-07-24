# Write a python function to print multiplication table for a number.

def multiply(n):
    for i in range(1 , 11):
        print(f"{n} X {i} = {n*i}")

multiply(6)