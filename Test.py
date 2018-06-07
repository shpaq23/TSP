import math
xs = 10
ys = 10

r = 8

x1 = []
y1 = []
for a in range(0, 361, 6):
    x = r * math.cos(math.radians(a)) + xs
    y = r * math.sin(math.radians(a)) + ys
    x = round(x, 3)
    y = round(y, 3)
    x1.append(x)
    y1.append(y)
try:
    file = open("circle.tsp", "w")
    for a in range(0, len(x1)):
        ver = str(a+1) + " " +str(x1[a]) +" "+ str(y1[a]) + "\n"
        file.writelines(ver)
except:
    print("blad")



print(x1)
print(y1)
