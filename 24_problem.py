s = {8, 7, 12,"Rishi" , [1,2]}

s.update({8, 7, 12}) # This will not work because sets cannot contain mutable types like lists.
print(s)  