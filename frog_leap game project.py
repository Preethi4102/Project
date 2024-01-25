positions = list(['G','G','G','-','B','B','B'])
print("[ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ]")
print(positions)

while True:
    pos = input("Press q to quit else \nEnter position of piece:")
    if pos == 'q':
        print("YOU LOSE!!")
        break
    pos = int(pos)

    if pos not in [0,1,2,3,4,5,6]:
        print("Invalid move")

    if positions[pos] == '-':
        print("Invalid move")
        continue

    if positions[pos] == 'G':
        if (pos + 1) <= 6 and positions[pos + 1] == '-':
            pos2 = (pos+1)
        elif (pos + 2) <= 6 and positions[pos + 2] == '-' and positions[pos + 1] == 'B':
            pos2 = (pos+2)
        else:
            print("Invalid move")

    if positions[pos] == 'B':
        if (pos - 1) >= 0 and positions[pos - 1] == '-':
            pos2 = (pos-1)
        elif (pos - 2) >= 0 and positions[pos - 2] == '-' and positions[pos - 1] == 'G':
            pos2 = (pos-2)
        else:
            print("Invalid move")

    pos2 = 0
    if positions[pos] == 'G':
        if positions[pos + 1] == '-':
            pos2 = (pos+1)
        elif positions[pos + 2] == '-':
            pos2 = (pos+2)
    if positions[pos] == 'B':
        if positions[pos - 1] == '-':
            pos2 = (pos-1)
        elif positions[pos - 2] == '-':
            pos2 = (pos-2)
    positions[pos], positions[pos2] = positions[pos2], positions[pos]

    print("[ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ]")
    print(positions)

    if positions == ['B','B','B','-','G','G','G']:
        print("YOU WIN")
        break