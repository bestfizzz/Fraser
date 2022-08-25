import tkinter as tk


hotel = [['A', 'A', 'A', 'A'],
       ['A', 'A', 'A', 'A'],
       ['O', 'O', 'R', 'R'],
       ['A', 'A', 'A', 'A']]

hotelButton = []
root = tk.Tk()

for i in range(len(hotel)):
        for j in range(len(hotel[i])):
            print(i,j)
            rN='{}.{}'.format(i+1,j+1)
            x='{}: {}'.format(rN,hotel[i][j])
            l =  tk.Button(text=''+x)
            l.config(height=3, 
			  width=15)
            l.grid(column=j, row=i, padx=5,pady=5,sticky="nsew")
            hotelButton.append(l)
            print(hotelButton)
            

root.mainloop()
