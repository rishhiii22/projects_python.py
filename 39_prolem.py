'''
***
* *    for n = 3
***

'''



n = int(input("Enter the number: "))
for i in range(1 , n+1):  # Agar mai range (n) leta hu to range (n-1) tk jayega kyuki ek kam jata hai hamesha to isliye hame range (n+1) liya taaki range (n) tk jaaye.
    if(i==1 or i==n):
        print("*"* n, end="")
    else:
        print("*", end="")
        print(" "* (n-2), end="")
        print("*", end="")
    print("")
