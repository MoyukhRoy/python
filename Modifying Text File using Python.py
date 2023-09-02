file = open('DIY Dataset/Poem.txt')
data = file.read()
for letter in data:
    if letter == 'J':
        print("K", end="")
    else:
        print(letter, end="")
file.close()