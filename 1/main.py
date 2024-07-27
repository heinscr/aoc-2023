# Creating a file
file1 = open("input2", "r+")

numbers = [["one","1"],["two","2"],["three","3"],["four","4"],["five","5"],["six","6"],["seven","7"],["eight","8"],["nine","9"]] 
lines = file1.readlines()
file1.close()

positions = []
for line in lines:
    position = []
    for value in numbers:
        pos = 0
        while line.find(value[0],pos) != -1:
            pos = line.find(value[0],pos)
            position.append([pos,value[1]])    
            pos+=1
    count=0
    for element in line:
        if element.isnumeric():
            position.append([count,element])
        count+=1;
    position.sort(key=lambda x:x[0])
    positions.append(position)
    for pos in position:
        print(pos)

count = 0
total = 0
for line in positions:
    first = 0
    second = 0
    for pos in line:
        if first == 0:
            first = int(pos[1])
            second = first
        else: 
            second = int(pos[1])
    count+=1
    print("Line{}: {}".format(count, first*10+second))
    total +=first*10+second
print(total)
