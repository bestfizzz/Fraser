
from functools import partial
import tkinter as tk
from tkinter.messagebox import showinfo
import firebaseTest
import os
from PIL import Image  
#get data
hotel = firebaseTest.getHotel()
#user= firebaseTest.getUser()
def getRoom(roomType):
      print(roomType)
      roomList=[]
      roomType=roomType.upper()
      #search for room that have the same roomTpye
      for floor in range(0,len(hotel)):
            for room in range(0,len(hotel[floor])):
                  print(floor,room)
                  if roomType==hotel[floor][room]:
                        roomList.append('{}0{}: {}'.format(floor+1,room+1,roomType))
      return roomList
def changeState(roomNumber,stateChange):
    stateChange=stateChange.upper()
    floor=int(roomNumber[:roomNumber.index("0")].strip())
    room=int(roomNumber[roomNumber.index("0")+1:].strip())
    #check if floor and room exist(no longer needed)
    if floor <= len(hotel):
        if room<= len(hotel[floor-1]):
          #may check if the user is the current owner via checkRoom  
          #stop user from making invailid changes
            if stateChange=='R' and hotel[floor-1][room-1]=='O':
                return 'Room already occupied'
            elif stateChange==hotel[floor-1][room-1]:
                return 'no change were made'
            else:
                hotel[floor-1][room-1]=stateChange
                firebaseTest.uploadHotel(hotel)
                return 'Success'
        else: 
            print("\nroom doesn't exist")
    else: 
        print("\nfloor doesn't exist")
class App(tk.Tk):
      def __init__(self):
            super().__init__()
            # configure the root window
            self.title('Buv sunshine hotel')
            self.geometry('535x480')
            frame=tk.Frame(self,padx=2,width=535,height=500,bg='white')
            frame.pack(side="top",fill='both',expand=True)
            frame.rowconfigure(0, weight= 3)
            frame.rowconfigure(1, weight= 1)
            frame.grid()
            self.image1 = tk.PhotoImage(file="./buv2.png")
            #run beging screen
            self.welcomeScreen(frame=frame)
      def welcomeScreen(self,frame):
            frame1=tk.Frame(frame,width=500,bg='white')
            frame1.rowconfigure(0,weight=1)
            frame1.rowconfigure(0,weight=1)
            frame2=tk.Frame(frame,pady=20,bg='white')
            frame2.columnconfigure(0,weight=1)
            frame2.columnconfigure(1,weight=1)
            frame2.columnconfigure(2,weight=1)
            frame1.grid(row=0,sticky="NWSE")
            frame2.grid(row=1,sticky="NWSE")
            welcomeText=tk.Label(frame1,text='WELCOME \n    TO \n      BUV SUNSHINE',font=("Arial", 35),bg='white')
            startBtn=tk.Button(frame2,text="start",command=partial(self.mainApp,frame,))
            exitBtn=tk.Button(frame2,text="exit",command=self.destroy)
            logoLable=tk.Label(frame1,image=self.image1,highlightthickness=0,borderwidth=0)
            welcomeText.grid(row=1,sticky="NWES")
            startBtn.grid(row=0,column=1,sticky='NWSE')
            exitBtn.grid(row=1,column=1,sticky='NWSE',pady=15)S
            logoLable.grid(row=0,sticky="W")
      def showAllRooms(self,frame,changeType=None):
            #configure
            frame1=tk.Frame(frame,width=500,padx=15,bg='red')
            frame1.grid(row=0,sticky="nsew")
            #display all rooms as buttons
            for floor in range(len(hotel)):
                  for room in range(len(hotel[floor])):
                        print(floor,room)
                        rN='{}0{}'.format(floor+1,room+1)
                        x='{}: {}'.format(rN,hotel[floor][room])
                        l =  tk.Button(frame1,text=''+x,command=partial(self.roomOnClick,rN,frame,changeType))
                        l.config(height=3, 
                  width=15,bg='white')
                        l.grid(column=room, row=floor, padx=5,pady=5,sticky="nsew")
      def showSomeRooms(self,frame,theList):
            #configure
            frame1=tk.Frame(frame,width=500,padx=15,bg='red')
            frame1.grid(row=0,sticky="nsew")
            j=0
            k=0
            #display rooms as buttons base on the list return from getList
            for i in range(len(theList)):
                  rN=theList[i]
                  l =  tk.Button(frame1,text=''+rN,command=partial(self.roomOnClick,rN,frame))
                  l.config(height=3, 
                  width=15,bg='white')
                  k=k+1
                  #max of 4 btn per row
                  if (i)%4==0:
                        j=j+1
                        k=0
                  l.grid(row=j,column=k ,padx=5,pady=5,sticky="nsew")
      def viewRoomQuote(self,frame,roomType):
            #configure
            frame2=tk.Frame(frame,pady=20,highlightbackground="black" , highlightthickness=1,height=50,bg='red')
            
            frame2.columnconfigure(0, weight= 3)
            frame2.columnconfigure(1, weight= 1)
            frame2.grid(row=1,sticky="nsew")
            #text display
            a = 'available' if roomType=='A' else 'occupied' if roomType=='O' else 'reserved'
            txt='Here are the {} rooms'.format(a)
            t=tk.Label(frame2,text=''+txt,bg="red")
            t.grid(column=0,sticky='w')
            #back button display
            exitBtn=tk.Button(frame2,text='back',command=partial(self.mainApp,frame))
            exitBtn.grid(column=1,padx=15,)
            exitBtn.config(height=3, 
                  width=15)
      def showAllRoomsScreen(self,frame):
            #show all rooms
            self.showAllRooms(frame=frame)
            #configure
            frame2=tk.Frame(frame,pady=20,highlightbackground="black" , highlightthickness=1,height=50,bg='red')
            frame2.columnconfigure(0, weight= 3)
            frame2.columnconfigure(1, weight= 1)
            frame2.grid(row=1,sticky="nsew")
            #text display
            txt='Here are all the rooms'
            t=tk.Label(frame2,text=''+txt,bg='red')
            t.grid(column=0,sticky='w')
            #back button display
            exitBtn=tk.Button(frame2,text='exit',command=partial(self.mainApp,frame))
            exitBtn.grid(column=1,padx=15,)
            exitBtn.config(height=3, 
                  width=15)
      def roomOnClick(self,roomnum,frame,changeType=None):
            #the make change function only runs when the action is chosen
            if changeType:  
                  mess=changeState(roomNumber=roomnum,stateChange=changeType)
                  self.mainApp(frame=frame)
                  tk.messagebox.showinfo(title='Operation', message=''+mess)
            else:
                  print(roomnum)  
      def mainControlPanel(self,frame):
            #configure
            frame2=tk.Frame(frame,pady=20,highlightbackground="black" , highlightthickness=1,height=50,bg='red')
            frame2.rowconfigure(0, weight= 3)
            frame2.rowconfigure(1, weight= 1)
            frame2.columnconfigure(0, weight= 1)
            frame2.columnconfigure(1, weight= 1)
            frame2.columnconfigure(2, weight= 1)
            frame2.grid(row=1,sticky="nsew")
            #book room
            bR=tk.Button(frame2,text='book room',command=partial(self.changeStateScreen,frame,"R"))
            bR.grid(column=0,row=0,padx=15, pady=15)
            bR.config(height=3, 
                  width=15)
             #take room
            tR=tk.Button(frame2,text='take room',command=partial(self.changeStateScreen,frame,"O"))
            tR.grid(column=0,row=1)
            tR.config(height=3, 
                  width=15)

            #cancel reserved room
            cRR=tk.Button(frame2,text='free up a room',command=partial(self.changeStateScreen,frame,"A"))
            cRR.grid(column=1,row=0)
            cRR.config(height=3, 
                  width=15)

            #view room
            vR=tk.Button(frame2,text='view room',command=partial(self.viewMenu,frame))
            vR.grid(column=1,row=1)
            vR.config(height=3, 
                  width=15)

            #exit
            exitBtn=tk.Button(frame2,text='back to title',command=partial(self.welcomeScreen,frame,))
            exitBtn.grid(column=2,row=0,padx=15, pady=15)
            exitBtn.config(height=3, 
                  width=15)

            #draw map
            mapBtn=tk.Button(frame2,text='map',command=partial(os.system,
            #'python3 "/home/minh.nh2@buv.edu.vn/Desktop/Fraser/turtleMap.py"'  
            'python3 "turtleMap.py"'
            #'py "turtleMap.py"'
            ))
            mapBtn.grid(column=2,row=1,padx=15, pady=15)
            mapBtn.config(height=3, 
                  width=15)
      def changeStateMenu(self,frame,changeType):
            #configure
            frame2=tk.Frame(frame,pady=20,highlightbackground="black" , highlightthickness=1,height=50,bg='red')
            frame2.columnconfigure(0, weight= 3)
            frame2.columnconfigure(1, weight= 1)
            frame2.grid(row=1,sticky="nsew")
            #text based on changeType
            a = 'free up' if changeType=='A' else 'take' if changeType=='O' else 'book'
            txt='choose the room you want to {}'.format(a)
            t=tk.Label(frame2,text=''+txt,bg='red')
            t.grid(column=0,sticky='w')
            #back btn
            exitBtn=tk.Button(frame2,text='back',command=partial(self.mainApp,frame))
            exitBtn.grid(column=1,padx=15,)
            exitBtn.config(height=3, 
                  width=15)
      def viewMenu(self,frame):
            #frame
            frame2=tk.Frame(frame,pady=20,highlightbackground="black" , highlightthickness=1,height=50,bg='red')
            frame2.rowconfigure(0, weight= 3)
            frame2.rowconfigure(1, weight= 1)
            frame2.columnconfigure(0, weight= 1)
            frame2.columnconfigure(1, weight= 1)
            frame2.columnconfigure(2, weight= 1)
            frame2.grid(row=1,sticky="nsew")
            #view booked room
            bR=tk.Button(frame2,text='see booked room',command=partial(self.viewRoomScreen,frame,"R"))
            bR.grid(column=0,row=0,padx=15, pady=15)
            bR.config(height=3, 
                  width=15)

            #view occupied room
            oR=tk.Button(frame2,text='see occupied room',command=partial(self.viewRoomScreen,frame,"O"))
            oR.grid(column=0,row=1)
            oR.config(height=3, 
                  width=15)

            #view available room
            vAR=tk.Button(frame2,text='see available room',command=partial(self.viewRoomScreen,frame,"A"))
            vAR.grid(column=1,row=0)
            vAR.config(height=3, 
                  width=15)

            #view all room
            vR=tk.Button(frame2,text='view all room',command=partial(self.showAllRoomsScreen,frame))
            vR.grid(column=1,row=1)
            vR.config(height=3, 
                  width=15)

            #back
            exitBtn=tk.Button(frame2,text='back',command=partial(self.mainApp,frame))
            exitBtn.grid(column=2,row=0,padx=15, pady=15)
            exitBtn.config(height=3, 
                  width=15)
      def viewRoomScreen(self,frame,roomType):
            #show room based on asked roomType
            theList=getRoom(roomType=roomType)
            self.showSomeRooms(frame=frame,theList=theList)
            self.viewRoomQuote(roomType=roomType,frame=frame)
      def changeStateScreen(self,frame,changeType):
            self.showAllRooms(frame=frame,changeType=changeType)
            self.changeStateMenu(frame=frame,changeType=changeType)
      def mainApp(self,frame):
            #main app screen
            self.showAllRooms(frame=frame)
            self.mainControlPanel(frame=frame)
      
if __name__ == "__main__":
  app = App()
  app.mainloop()
