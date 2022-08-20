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
            hotel[floor-1][room-1]=stateChange.upper()
            print(hotel)
        else: 
            print("room doesn't exist")
    else: 
        print("floor doesn't exist")
def showAllRooms():
    for i in range(0,len(hotel)):
        for j in range(0,len(hotel[i])):
            print('{}.{}:{}'.format(i+1,j+1,hotel[i][j]),end=" ")
        if i<len(hotel)-1:
            print('\n')

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
showRooms('R')

changeState('4.5','o')
showAllRooms()
# a = int(input('Enter a number (-1 to quit): '))
  
# while a != -1:
#     a = int(input('1 to view rooms\n-1 to quit)\nEnter a number: '))