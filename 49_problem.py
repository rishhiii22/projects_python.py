# Write a program to read a text from a given file 'poem1.txt' and find out weather it contains the word 'twinke'.

f = open("poem1.txt")
content = f.read()
if("twinkle" in content):
    print("twinkle is present in content")
else:
    print("twinkle is not present in content")
f.close()

# Output;- "twinkle is present in content".

