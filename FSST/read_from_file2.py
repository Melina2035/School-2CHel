f = open("zahlen2.txt","r")
x = f.readlines()
print(x)
f.close()

f = open("zahlen2.txt", "r")
x2 = f.readline()
print(x2)
f.close()

f = open("zahlen2.txt", "r")
x2 = f.read()                                                           
print(x2)
f.close()

f = open("zahlen2.txt", "r")
while True:
	x = f.readline()
	print(x)
	if not x:
		break
f.close()


f = open("zahlen2.txt", "r")
for line in f:
	print(line)
f.close()

