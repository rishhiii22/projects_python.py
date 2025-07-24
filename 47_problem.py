
# Write a python program to remove a given word from a list ans strip it at the same time.
def rem(l , word):
    n =[]
    for item in l:
        if not(item == word):
         n.append(item.strip(word)) # Strip function starting or end se koi bhi word nikal deta hai 
    return n 

l = ["Rishi","Rohan","Shyam","Ram" , "am"]
print(rem(l ,"am"))

# We have removed a word and also striped it at same time using strip function.