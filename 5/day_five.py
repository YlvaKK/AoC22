stacks = [[],[],[],[],[],[],[],[],[]]

def crate_mover_9001(boxes, fstack, tstack):
    temp_stack = []
    for i in range(boxes):
        temp_stack.append(stacks[fstack].pop())

    for i in range(boxes):
        stacks[tstack].append(temp_stack.pop())

def crate_mover_9000(boxes, fstack, tstack):
    for i in range(boxes):
        stacks[tstack].append(stacks[fstack].pop())

with open('5/day_five_input.txt') as f:

    lines = [0]*8
    for i in range(7,-1, -1):
        lines[i] = f.readline()

    for row in lines:
        for column in range(0, 9):
            if row[column*4] == '[':
                stacks[column].append(row[(column*4)+1])

    f.readline()
    f.readline()

    while True:
        line = f.readline()
        if not line:
            break
        instruction = line.split(' ')

        boxes = int(instruction[1])
        fstack = int(instruction[3]) - 1
        tstack = int(instruction[5]) - 1

        crate_mover_9001(boxes, fstack, tstack)
    
    output = ""
    for stack in stacks:
        output = output + stack.pop()

    print(output)

        
    
