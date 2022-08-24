from operator import le
from re import X
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
    self.config()
    # configure the root window
    # self.title('My Awesome App')
    self.geometry('{}x{}'.format(500,500))
    # btmFrame=Frame(self)
    # btmFrame.grid(side='bottom')
    # topFrame=Frame(self)
    # topFrame.grid(side=TOP)
    # for i in range(len(hotel)):
    #     for j in range(len(hotel[i])):
    #         print(i,j)
    #         rN='{}.{}'.format(i+1,j+1)
    #         x='{}: {}'.format(rN,hotel[i][j])
    #         l =  tk.Button(topFrame,text=''+x)
    #         l.config(height=3, 
	# 		  width=15)
    #         l.grid(column=j, row=i, padx=5,pady=5,sticky="nsew")
        

    # label
    self.toolbar = tk.Frame( background="#d5e8d4", height=40)
    self.statusbar = tk.Frame( background="#e3e3e3", height=20)
    self.main = tk.PanedWindow( background="#99fb99")

    self.toolbar.pack(side="top", fill="x")
    self.statusbar.pack(side="bottom", fill="x")
    self.main.pack(side="top", fill="both", expand=True)

    
  def button_clicked(self):
    showinfo(title='Information', message='Hello, Tkinter!')

if __name__ == "__main__":
  app = App()
  app.mainloop()