
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
#from firebase_admin import auth

# Application Default credentials are automatically created.
cred = credentials.Certificate('tkintersuck-firebase-adminsdk-rbz5s-e3cf33b1c0.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection(u'BUV ss').document(u'Hotel')
#only works with strong internet connection
def uploadHotel(hotel):
    global doc_ref
    try:
        #upload list in 4 parts(floor)
        doc_ref.set({
        u'f1':hotel[0],
        u'f2':hotel[1],
        u'f3':hotel[2],
        u'f4':hotel[3]})
        return True
    except:
        return False

def getHotel():
    hotel=[]
    for i in doc_ref.get().to_dict():
        hotel.insert(0,doc_ref.get().to_dict()[i])
    return hotel
#auth is useless without firebase async client, python's async await just doesnt work.
# def makeUser(data):
#     auth.create_user(
#     email=f'{data.email}',
#     password=f'{data.password}')
#     db.collection(u'user').document(f'{data.email}')
#def addUserRoom(roomNumber,email):
    # data=db.collection(u'user').document(f'{email}').room.append(roomNumber)
    # db.collection(u'user').document(f'{email}').set({room:[data]})
#def delUserRoom(roomNumber,email):
    # data=db.collection(u'user').document(f'{email}').room.splice(roomNumber,1)
    # db.collection(u'user').document(f'{email}').set({room:[data]})
# def getUser(email):
#     return auth.get_user_by_email(email)
# def checkRoom(roomNumber,changeType,email):
