from tkinter import *
import random
import time
tk= Tk()
tk.configure(bg="tomato")
Height = 1080
Width = 1920

canvas = Canvas(tk,width = Width,height= Height)

tk.title("Graphics")
canvas.pack()

ball = canvas.create_oval(100,100,2,1)
xspeed = 5
yspeed = 0

tk.state("zoomed")

while True :

    canvas.move(ball,xspeed,yspeed)
    pos = canvas.create_text(ball)

    if pos[2]>=Width:
        xspeed = -xspeed

    tk.update()
    time.sleep(0.1)
