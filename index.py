from operator import le

valid=['A','R','O']
hotel = [['A', 'A', 'A', 'A'],
       ['A', 'A', 'A', 'A'],
       ['O', 'O', 'R', 'R'],
       ['A', 'A', 'A', 'A']]

def logRoom(roomlist, roomType):
    a = 'available' if roomType=='A' else 'occupied' if roomType=='O' else 'reserved'
    print('The {} rooms are: '.format(a),', '.join(roomlist))

def changeState(roomNumber,stateChange):
    stateChange=stateChange.upper()
    if stateChange not in valid:
        return print('invalid state input')
    floor=int(roomNumber[:roomNumber.index(".")].strip())
    room=int(roomNumber[roomNumber.index(".")+1:].strip())
    if floor <= len(hotel):
        if room<= len(hotel[floor-1]):
            if stateChange=='R' and hotel[floor-1][room-1]=='O':
                print('Room already occupied')
            elif stateChange==hotel[floor-1][room-1]:
                print('no change were made')
            else:
                hotel[floor-1][room-1]=stateChange
                print(hotel)
        else: 
            print("\nroom doesn't exist")
    else: 
        print("\nfloor doesn't exist")
def showAllRooms():
    for i in range(0,len(hotel)):
        for j in range(0,len(hotel[i])):
            print('{}.{}:{}'.format(i+1,j+1,hotel[i][j]),end=" ")
        print('\t')

def showRooms(roomType):
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
print('WELLCOME TO HOTEL')
while True:
    print('\nmanual:\n4 to cancel booked rooms\n3 to book rooms\n2 to take rooms\n1 to view rooms\n-1 to quit\n')
    a = input('Enter a number: ')
    validInput=['-1','1','2','3','4']
    if a not in validInput:
        print('invalid input')
    else:
        a=int(a)
        if a==1:
            while True:
                print('\nmaunal\n4 to see booked rooms\n3 to see occupied rooms\n2 to see available rooms\n1 to view all rooms\n-1 to go back to menu\n')
                b = input('Enter b number: ')
                if b not in validInput:
                    print('invalid input')
                    a=1
                else:
                    b=int(b)
                    if b>=2 and b<=4:
                        case=['A','O','R']
                        showRooms(case[b-2])
                        a=1
                    elif b==1:
                        print("here are the all rooms: ")
                        showAllRooms()
                    elif b==-1:
                        break
        elif a>=2 and a<=4:
            case=[['take','O'],['book','R'],['cancel','A']]
            print('aaaaaaa')
            b=input('Enter room number(floor.room) you want to {}: '.format(case[a-2][0]))
            changeState(b,case[a-2][1])
        elif a==-1:
            print('Good bye')
            break
        else:
            print('invalid input')
    showAllRooms()