name_file=input("Enter file name:")
try:
    file=open(name_file)
except:
    print("file not correct")
    quit()
box=[]
for line in file:
    word_uni= line.split()
    for word in word_uni:
        if word not in box:
            box.append(word)
    box.sort()
print(box)
