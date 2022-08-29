import tkinter as tk
from turtle import *

hotel = [['A', 'A', 'A', 'A'],
       ['A', 'A', 'A', 'A'],
       ['O', 'O', 'R', 'R'],
       ['A', 'A', 'A', 'A']]
speed(10)
def drawRoom():
    for z in range(4):
        forward(40)
        left(90)
def drawFloor(floorNumber):
    for j in range(len(hotel[floorNumber])):
        drawRoom()
        forward(40)
def drawHotel():
    for i in range(len(hotel)):
        drawFloor(i)
        drawHallway()
        if i == len(hotel)-1:
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

