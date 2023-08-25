import random


color = ["R", "G", "B"]

data = {}

for i in range(1, 25):
    data[i] = []
    for j in range(46):
        data[i].append(color[random.randrange(0, 3)])
    
    
print(data)