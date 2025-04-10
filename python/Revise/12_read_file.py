#read file
f = open("funny.txt", "r")
for line in f:
    print(line)
f.close()

#readlines()
f = open("funny.txt", "r")
lines = f.readlines()
print(lines)

#write file
f = open('love.txt', 'w')
f.write("I love python")
f.close()

# same file when you write i love javascript the previous line goes away
f = open('love.txt','w')
f.write("I love JS")
f.close()

# You can use append mode to stop having previous lines overwritten
f = open("love.txt", "a")
f.write("I love javascript")
f.close()

# writelines
f = open("love.txt", "w")
f.writelines(["I love C++\n","I love scala"])
f.close()

# with statement
with open("funny.txt", "r") as f:
    for line in f:
        print(line)

