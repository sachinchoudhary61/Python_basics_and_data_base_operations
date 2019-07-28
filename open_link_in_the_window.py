import tkinter as t
import webbrowser
root = t.Tk()

def Open_itch():
    webbrowser.open("http://www.uiit.ac.in/")

button = t.Button(root,text="",command = Open_itch)
button.grid(row=0,column=0)

root.mainloop()
