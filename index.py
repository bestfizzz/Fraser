hotel = [['A', 'A', 'A', 'A'],
       ['A', 'A', 'A', 'A'],
       ['O', 'O', 'R', 'R'],
       ['A', 'A', 'A', 'A']]

def logRoom(roomlist, roomType):
    a = 'available' if roomType=='A' else 'occupied' if roomType=='O' else 'reserved'
    print('The {} rooms are: '.format(a),', '.join(roomlist))

def changeState(roomNumber,stateChange):
    floor=int(roomNumber[:roomNumber.index(".")].strip())
    room=int(roomNumber[roomNumber.index(".")+1:].strip())
    hotel[floor-1][room-1]=stateChange.upper()
    print(hotel)

def showRooms(roomType):
    valid=['A','R','O']
    roomList=[]
    roomType=roomType.upper()
    if roomType not in valid:
        return print('invalid input')
        
    for i in range(0,len(hotel)):
        for j in range(0,len(hotel[i])):
            if roomType==hotel[i][j]:
                roomList.append('{}.{}'.format(i+1,j+1))
            j=j+1
        i=+1
    return logRoom(roomList,roomType)
showRooms('R')
changeState('3.4','o')