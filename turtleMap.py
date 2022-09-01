
import tkinter as tk
from turtle import *
hotel = [['A', 'A', 'A', 'A'],
       ['A', 'A', 'A', 'A'],
       ['O', 'O', 'R', 'R'],
       ['A', 'A', 'A', 'A']]

speed(10)
def drawRoom(floorNumber,roomNumber):
    for i in range(4):
        forward(40)
        left(90)
    write('{}0{}'.format(floorNumber+1,roomNumber+1))
def drawFloor(floorNumber):
    for room in range(len(hotel[floorNumber])):
        drawRoom(floorNumber,room)
        forward(40)
def drawHotel():
    for floor in range(len(hotel),0,-1):
        drawFloor(floor-1)
        drawHallway()
        if floor == 1:
            continue
        else:
            forward(40)
            left(90)
def drawHallway():
    right(90) 
    forward(40)
    right(90)  
    forward(160)
    right(90)
    forward(40)
    right(180)
    forward(40)
drawHotel()
done()

