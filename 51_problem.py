
import os

def generateTable(n):
    table = ""
    # Ensure the 'tables' directory exists
    os.makedirs("tables", exist_ok=True)
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"

        with open(f"tables/table_{n}.txt", "w") as f:
            f.write(table)
    
    
    
    for i in range(2, 21):
        generateTable(i)
