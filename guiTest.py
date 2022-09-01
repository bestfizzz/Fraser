
from functools import partial
from telnetlib import X3PAD
from textwrap import fill
import tkinter as tk
from tkinter import BOTTOM, CENTER, TOP, X, Frame, Text, ttk
from tkinter.messagebox import showinfo

hotel = [['A', 'A', 'A', 'A'],
       ['A', 'A', 'A', 'A'],
       ['O', 'O', 'R', 'R'],
       ['A', 'A', 'A', 'A']]
def getRoom(roomType):
      print(roomType)
      roomList=[]
      roomType=roomType.upper()
      for i in range(0,len(hotel)):
            for j in range(0,len(hotel[i])):
                  print(i,j)
                  if roomType==hotel[i][j]:
                        roomList.append('{}.{}'.format(i+1,j+1))
                        j=j+1
            i=+1
      return roomList
def changeState(roomNumber,stateChange):
    stateChange=stateChange.upper()
    floor=int(roomNumber[:roomNumber.index(".")].strip())
    room=int(roomNumber[roomNumber.index(".")+1:].strip())
    if floor <= len(hotel):
        if room<= len(hotel[floor-1]):
            if stateChange=='R' and hotel[floor-1][room-1]=='O':
                return 'Room already occupied'
            elif stateChange==hotel[floor-1][room-1]:
                return 'no change were made'
            else:
                hotel[floor-1][room-1]=stateChange
                return 'Success'
        else: 
            print("\nroom doesn't exist")
    else: 
        print("\nfloor doesn't exist")
class App(tk.Tk):
      def __init__(self):
            super().__init__()
            # configure the root window
            # self.title('My Awesome App')
            self.geometry('400x500')
            frame=tk.Frame(self,padx=2,width=500,height=500)
            frame.pack(side=TOP,fill='both',expand=True)
            frame.rowconfigure(0, weight= 3)
            frame.rowconfigure(1, weight= 1)
            frame.grid()
            self.mainApp(frame=frame)
      def showAllRooms(self,frame,changeType=None):
            frame1=tk.Frame(frame,bg="red",width=500,padx=15)
            frame1.grid(row=0,sticky="nsew")
            for i in range(len(hotel)):
                  for j in range(len(hotel[i])):
                        print(i,j)
                        rN='{}.{}'.format(i+1,j+1)
                        
                        x='{}: {}'.format(rN,hotel[i][j])
                        l =  tk.Button(frame1,text=''+x,command=partial(self.roomOnClick,rN,frame,changeType))
                        l.config(height=3, 
                  width=10)
                        l.grid(column=j, row=i, padx=5,pady=5,sticky="nsew")
      def showSomeRooms(self,frame,theList):
            frame1=tk.Frame(frame,bg="red",width=500,padx=15)
            frame1.grid(row=0,sticky="nsew")
            j=0
            k=0
            for i in range(len(theList)):
                  rN=theList[i]
                  l =  tk.Button(frame1,text=''+rN,command=partial(self.roomOnClick,rN,frame))
                  l.config(height=3, 
                  width=10)
                  k=k+1
                  if (i)%4==0:
                        j=j+1
                        k=0
                  l.grid(row=j,column=k ,padx=5,pady=5,sticky="nsew")
      def viewRoomQuote(self,frame,roomType):
            #text display
            a = 'available' if roomType=='A' else 'occupied' if roomType=='O' else 'reserved'
            txt='Here are the {} rooms'.format(a)
            frame2=tk.Frame(frame,pady=20,highlightbackground="black" , highlightthickness=1,height=50)
            frame2.columnconfigure(0, weight= 3)
            frame2.columnconfigure(1, weight= 1)
            frame2.grid(row=1,sticky="nsew")
            
            t=tk.Label(frame2,text=''+txt)
            t.grid(column=0,sticky='w')
            exitBtn=tk.Button(frame2,text='exit',command=partial(self.mainApp,frame))
            exitBtn.grid(column=1,padx=15,)
            exitBtn.config(height=3, 
                  width=15)
      def showAllRoomsScreen(self,frame):
            self.showAllRooms(frame=frame)
            #configure
            frame2=tk.Frame(frame,pady=20,highlightbackground="black" , highlightthickness=1,height=50)
            frame2.columnconfigure(0, weight= 3)
            frame2.columnconfigure(1, weight= 1)
            frame2.grid(row=1,sticky="nsew")
            txt='Here are all the rooms'
            t=tk.Label(frame2,text=''+txt)
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
            frame2=tk.Frame(frame,pady=20,highlightbackground="black" , highlightthickness=1,height=50)
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
            exitBtn=tk.Button(frame2,text='exit',command=self.destroy)
            exitBtn.grid(column=2,row=0,padx=15, pady=15)
            exitBtn.config(height=3, 
                  width=15)
      def changeStateMenu(self,frame,changeType):
            #configure
            frame2=tk.Frame(frame,pady=20,highlightbackground="black" , highlightthickness=1,height=50)
            frame2.columnconfigure(0, weight= 3)
            frame2.columnconfigure(1, weight= 1)
            frame2.grid(row=1,sticky="nsew")
            #text based on changeType
            a = 'free up' if changeType=='A' else 'take' if changeType=='O' else 'book'
            txt='choose the room you want to {}'.format(a)
            t=tk.Label(frame2,text=''+txt)
            t.grid(column=0,sticky='w')
            #back btn
            exitBtn=tk.Button(frame2,text='back',command=partial(self.mainApp,frame))
            exitBtn.grid(column=1,padx=15,)
            exitBtn.config(height=3, 
                  width=15)
      def viewMenu(self,frame):
            #frame
            frame2=tk.Frame(frame,pady=20,highlightbackground="black" , highlightthickness=1,height=50)
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
            vR=tk.Button(frame2,text='view room',command=partial(self.showAllRoomsScreen,frame))
            vR.grid(column=1,row=1)
            vR.config(height=3, 
                  width=15)

            #back
            exitBtn=tk.Button(frame2,text='back',command=partial(self.mainApp,frame))
            exitBtn.grid(column=2,row=0,padx=15, pady=15)
            exitBtn.config(height=3, 
                  width=15)
      def viewRoomScreen(self,frame,roomType):
            theList=getRoom(roomType=roomType)
            self.showSomeRooms(frame=frame,theList=theList)
            self.viewRoomQuote(roomType=roomType,frame=frame)
      def changeStateScreen(self,frame,changeType):
            self.showAllRooms(frame=frame,changeType=changeType)
            self.changeStateMenu(frame=frame,changeType=changeType)
      def mainApp(self,frame):
            self.showAllRooms(frame=frame)
            self.mainControlPanel(frame=frame)
      
if __name__ == "__main__":
  app = App()
  app.mainloop()
