#  5! = 1 X 2 X 3 X 4 X 5

n = int(input("Enter the number: "))
product = 1
for i in range(1 , n+1):
    product = product * i

print(f"The factorial of {n} is {product}")

    # Agar mai range (n) leta hu to range (n-1) tk jayega kyuki ek kam jata hai hamesha to isliye hame range (n+1) liya taaki range (n) tk jaaye.
