
import tkinter as tk
from tkinter import BOTTOM, CENTER, TOP, Frame, ttk
from tkinter.messagebox import showinfo

hotel = [['A', 'A', 'A', 'A'],
       ['A', 'A', 'A', 'A'],
       ['O', 'O', 'R', 'R'],
       ['A', 'A', 'A', 'A']]

class App(tk.Tk):
  def __init__(self):
    super().__init__()
    # configure the root window
    # self.title('My Awesome App')
    self.geometry('{}x{}'.format(500,500))
    frame=tk.Frame(self,padx=2)
    frame.pack(side=TOP)
    frame.rowconfigure(0, weight= 3)
    frame.rowconfigure(1, weight= 1)
    frame1=tk.Frame(frame,bg="red")
    frame2=tk.Frame(frame,pady=20,highlightbackground="black" , highlightthickness=1,)
    frame2.rowconfigure(0, weight= 3)
    frame2.rowconfigure(1, weight= 1)
    frame2.columnconfigure(0, weight= 1)
    frame2.columnconfigure(1, weight= 1)
    frame2.columnconfigure(2, weight= 1)
    frame.grid()
  
    frame1.grid(row=0)
    frame2.grid(row=1)
    #book room
    bR=tk.Button(frame2,text='book room')
    bR.grid(column=0,row=0,padx=15, pady=15)
    bR.config(height=3, 
          width=15)

    #take room
    tR=tk.Button(frame2,text='take room')
    tR.grid(column=0,row=1)
    tR.config(height=3, 
          width=15)

    #cancel reserved room
    cRR=tk.Button(frame2,text='cancel reserved room')
    cRR.grid(column=1,row=0)
    cRR.config(height=3, 
          width=15)

    #view room
    vR=tk.Button(frame2,text='view room')
    vR.grid(column=1,row=1)
    vR.config(height=3, 
          width=15)

    #exit
    exitBtn=tk.Button(frame2,text='exit')
    exitBtn.grid(column=2,row=0,padx=15, pady=15)
    exitBtn.config(height=3, 
          width=15)

    def showAllRooms(frame1):
      for i in range(len(hotel)):
          for j in range(len(hotel[i])):
              print(i,j)
              rN='{}.{}'.format(i+1,j+1)
              x='{}: {}'.format(rN,hotel[i][j])
              l =  tk.Button(frame1,text=''+x)
              l.config(height=3, 
          width=10)
              l.grid(column=j, row=i, padx=5,pady=5,sticky="nsew")
    showAllRooms(frame1)


    # label

  def button_clicked(self):
    showinfo(title='Information', message='Hello, Tkinter!')

if __name__ == "__main__":
  app = App()
  app.mainloop()