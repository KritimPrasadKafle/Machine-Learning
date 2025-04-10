# f = open("D:/Hustle/Python/Practice/funny.txt", "w")
# f.write("I love Python")
# f.close()
#
# f = open("D:/Hustle/Python/Practice/funny1.txt", "a")
# f.write("\nHaina Hola")
# f.close()
#
#
f = open("D:/Hustle/Python/Practice/funny1.txt", "r")
# print(f.read())
# f.close()

f_out = open("D:\Hustle\Python\Practice\gunncy_wc.txt", "w")
for line in f:
    tokens = line.split(' ')
    f_out.write(line+" wordcount: "+ str(len(tokens)))
    print(str(tokens))
f.close()

f_out.close()
