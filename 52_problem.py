word = "Donkey"

with open("file.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word,"Monkey")

with open("file.txt", "w") as f:
    content = f.write(contentNew)
