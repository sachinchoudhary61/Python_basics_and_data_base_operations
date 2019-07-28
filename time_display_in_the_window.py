import tkinter as t
import time

def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200,tick)
root = t.Tk()
clock = t.Label(root,font="Century 10 bold",fg="white",bg="black")
clock.grid(row=0,column=1)
tick()
root.mainloop()
