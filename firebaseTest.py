
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Application Default credentials are automatically created.
cred = credentials.Certificate('tkintersuck-firebase-adminsdk-rbz5s-e3cf33b1c0.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection(u'BUV ss').document(u'Hotel')
def uploadHotel(hotel):
    global doc_ref
    try:
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
        hotel.append(doc_ref.get().to_dict()[i])
    return hotel