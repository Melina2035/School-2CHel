f = open("zahlen.txt","r")
x = f.readlines()
print(x)
f.close()

f = open("zahlen.txt", "r")
x2 = f.readline()
print(x2)
f.close()

f = open("zahlen.txt", "w")
f.write(str(x))
f.write("Juhuuuu")
f.close()

f=open("zahlen.txt", "a")
f.write("hello world")

