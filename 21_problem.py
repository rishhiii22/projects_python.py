s = set()
s.add(18)
s.add("18")

print(s)  # This will print the set containing the numbers entered because sets do not allow duplicates.

s = set()
s.add(20) 
s.add("20") 
s.add(20.0) 

print(len(s))  # This will print the set containing the numbers entered, demonstrating that sets treat 20, "20", and 20.0 as distinct elements.