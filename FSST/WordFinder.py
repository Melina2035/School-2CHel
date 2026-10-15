import sys

inP = sys.argv[1]
outP = sys.argv[2]

dataR = open(inP, "r")
dataW = open(outP, "a")

while True:
    x = dataR.readline()

    for i in range(len(x)):
        if x[i].lower() == x[i+1].lower():
            dataW.write(x)
            print("FOUND")
        if not i:
            break

    if not x:
        break

dataR.close()
dataW.close()

